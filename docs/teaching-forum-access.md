# Teaching Forum: access requests and the auto-reply

Maintainer notes. This folder is excluded from the Jekyll build, so nothing here is published.

## How the pieces fit

| Piece | Where | Who sees it |
|---|---|---|
| Request page with the "Email a request" button | `/teaching-forum/`, in the site nav | Everyone |
| Notes page | `/teaching-forum/notes-6da5be14/`, linked from nowhere, `noindex` | People who were sent the link |
| Allow-list and "already sent" log | An Excel workbook in your Penn OneDrive, never in this repository | You and Bhuv |
| Auto-reply | A Power Automate flow on your Penn mailbox | Runs on its own |

The button is a `mailto:` link. It opens the visitor's own mail app with your address filled in, the subject line **Teaching Forum access request**, and a short body asking for name, department and courses. The visitor sends it. The subject line is the trigger for the flow, so if you change it in `pages/teaching-forum.md`, change it in the flow too.

What the flow does on every email whose subject contains that string:

1. Drop it unless the subject is *exactly* that string. Replies ("RE:"), forwards ("FW:") and out-of-office messages ("Automatic reply:") never match, so nobody gets a second email for following up.
2. Drop it unless the sender address ends in `@upenn.edu` or `.upenn.edu` (so `sas.upenn.edu` counts).
3. Look the sender up in the `Allowlist` table. Not there: do nothing except flag the message so you see it.
4. Look the sender up in the `Sent` table. Already there: do nothing except flag it.
5. Otherwise reply, in the same thread, with the link, and add the sender to `Sent`.

Silence for people not on the list is deliberate. A "sorry, no" reply would confirm that a list exists, and it can start loops with other people's auto-replies.

## Before you build the flow

1. **Check you have Power Automate.** Sign in at <https://make.powerautomate.com> with your PennKey. If you land on a home page with a "Create" item in the left rail, you have it. If it asks you to start a trial or buy a license, stop here and keep replying by hand; the rest of this file does not apply.
2. **Make the workbook.** In OneDrive (your Penn account), create `Teaching Forum access.xlsx` with two sheets. On each sheet put the header in A1, select it, and use *Insert → Table* with "My table has headers" ticked, then rename the table in *Table Design → Table Name*:
   - Sheet 1, table **Allowlist**, one column **Email**. One row per address, lower-case. Put in every alias a person might send from, for example both `jsmith@upenn.edu` and `jsmith@sas.upenn.edu`.
   - Sheet 2, table **Sent**, two columns **Email** and **SentAt**. Leave it empty.
   
   Keep this file out of the repository. It is a list of colleagues' addresses.
3. **Decide the reply text.** A draft is at the end of this file.

## Build the flow

In Power Automate: *Create → Automated cloud flow*. Name it `Teaching Forum access reply`, pick the trigger **When a new email arrives (V3)** from the Office 365 Outlook connector, and create. Then add the steps below in order. Action names are as the connector shows them today; the editor may label a few slightly differently.

Where a step says *expression*, click into the field, choose the **Expression** tab (the *fx* button) and paste the text. Do not put expressions into the plain-text tab, or they will be sent literally.

**1. Trigger: When a new email arrives (V3)**
- Folder: `Inbox`
- Show advanced options → Subject Filter: `Teaching Forum access request`
- Include Attachments: `No`. Everything else default.

The subject filter is a "contains" match, which is why step 3 exists.

**2. Initialize variable**
- Name: `sender`, Type: `String`
- Value, expression:
  ```
  toLower(trim(triggerOutputs()?['body/from']))
  ```

**3. Condition: exact subject**
- Left side, expression:
  ```
  equals(trim(triggerOutputs()?['body/subject']), 'Teaching Forum access request')
  ```
- Operator: `is equal to`. Right side, expression: `true`
- In the **If no** branch add **Terminate**, Status `Cancelled`. Leave **If yes** empty; the next steps go after the condition, not inside it.

**4. Condition: Penn address**
- Left side, expression:
  ```
  or(endsWith(variables('sender'), '@upenn.edu'), endsWith(variables('sender'), '.upenn.edu'))
  ```
- Operator `is equal to`, right side expression `true`. **If no** → Terminate, Cancelled.

**5. List rows present in a table** (Excel Online (Business))
- Location: `OneDrive for Business`. Document Library: `OneDrive`. File: pick `Teaching Forum access.xlsx`. Table: `Allowlist`.
- Rename the action to `List Allowlist` (click the title → Rename). The expressions below use these names.

**6. Filter array** (Data Operation)
- From: the `value` output of *List Allowlist* (pick it from the dynamic content panel).
- Switch the condition to **advanced mode** and paste:
  ```
  @equals(toLower(item()?['Email']), variables('sender'))
  ```
- Rename to `Allowlist match`.

**7. List rows present in a table** again, same file, Table `Sent`. Rename to `List Sent`.

**8. Filter array** again, From = `value` of *List Sent*, same advanced expression. Rename to `Already sent`.

**9. Condition: allowed and not yet sent**
- Left side, expression:
  ```
  and(greater(length(body('Allowlist_match')), 0), equals(length(body('Already_sent')), 0))
  ```
  (Power Automate turns the spaces in action names into underscores inside expressions.)
- Operator `is equal to`, right side `true`.

**If yes:**
- **Reply to email (V3)** (Office 365 Outlook). Message Id: the trigger's *Message Id* from dynamic content. Reply All: `No`. Body: the reply text below. The body is HTML; put the link on its own line.
- **Add a row into a table** (Excel): same file, Table `Sent`. Email: `variables('sender')` as an expression. SentAt, expression: `utcNow()`.

**If no:**
- **Flag email (V2)** (Office 365 Outlook), Message Id from the trigger. Nothing is sent. The request stays in your inbox, flagged, for you to decide by hand.

Save. The flow checker should report no errors.

## Test it

1. Add one of your own addresses to `Allowlist`.
2. Open the live request page (or the local preview) and click the button, or just send yourself an email with the exact subject.
3. Within a minute or two the flow should run (see *My flows → the flow → 28-day run history*), you should get the reply in the same thread, and `Sent` should have a row.
4. Send the same request again: no reply this time, the message is flagged.
5. Reply to the auto-reply with "thanks": nothing happens, because the subject now starts with "RE:".
6. Delete your rows from `Allowlist` and `Sent` when done.

## Day to day

- **Add someone:** add a row to `Allowlist`. The flow reads the file on every run, so there is nothing to republish.
- **Someone asks a second time:** delete their row from `Sent`, or just reply by hand.
- **A flagged request from someone not on the list:** decide, then either add them and reply by hand, or leave it.
- **Change the link or the wording:** edit the *Reply to email* step.
- **Pause:** *My flows → … → Turn off*. Requests then sit in your inbox like any other email.
- **Make the forum public:** follow the comment at the top of `pages/teaching-forum-notes.md`, deploy, then turn the flow off.

## Limits worth knowing

- **The connection is to your whole mailbox.** No mail API can grant "only this subject". The trigger's subject filter and the exact-match condition are what keep the flow to these messages, so keep the flow small and do not add steps that read other mail. If the forum grows, ask SAS Computing for a shared mailbox such as `teaching-forum@sas.upenn.edu` and move the flow there; then the flow's permission is scoped to that mailbox alone.
- **A forged From address cannot steal the link.** The reply goes to the From address, which would be the real person's mailbox, not the forger's.
- **The link can be forwarded.** Nothing stops a recipient passing it on; the page asks them not to.
- **The repository is public.** The notes page's address and content are readable on GitHub by anyone who looks. The team has accepted this. The address is unguessable from the site itself, which is all the random suffix is for.
- **Someone edits the subject line** in their mail app: the flow ignores the message and you handle it by hand. No harm done.
- **Excel connector quirks:** the file must stay where it is and keep its name; the tables must stay formatted tables (not plain ranges); the connector reads at most a few hundred rows per call, which is far more than this list will reach.

## Reply text

Subject is set automatically ("RE: Teaching Forum access request"). Body:

> Hi,
>
> Thanks for your interest in the Teaching Forum. The notes are here:
>
> https://ai-resources.datascience.sas.upenn.edu/teaching-forum/notes-6da5be14/
>
> The page is shared by invitation and is not linked from the site, so please keep this message rather than bookmarking it somewhere public, and don't forward the link. Colleagues who would like to read along can request access at https://ai-resources.datascience.sas.upenn.edu/teaching-forum/.
>
> If you would like to join the next session, just reply to this email.
>
> Elena Liang
> Data Driven Discovery Initiative, Penn Arts & Sciences
