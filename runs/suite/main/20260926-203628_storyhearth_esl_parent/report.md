# UserQA report: Minh Tran on http://127.0.0.1:8765/

*Persona:* **Minh Tran** (33) - Recently-arrived parent reading English as a second language (CEFR B1).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 12 steps | *Pages reviewed:* 9 | *Issues:* 26 | *LLM calls:* 15 | *Wall time:* 324.8 s

## What the agent understood the website to be
- **what it is:** A website for creating personalised, illustrated family storybooks.
- **who it is for:** Parents and families who want a story starring their child and another loved one.
- **value proposition:** Turn a family memory into an illustrated storybook, with a free digital preview and an option to print hardcovers.
- **pricing model:** The digital preview is described as free. Printed hardcovers are available, but no price is shown on this page.
- **fit for me:** It may be relevant because I want a story for Linh that includes our family and the lantern festival memory. I need simple language, careful cultural details, and a clear hardcover price.
- **main tasks:** Log in, Enter a child and another character, Share a family memory, place, and treasured object, Read the generated storybook preview, Check the price of a printed hardcover, Continue to checkout without paying

## Scores
- SUS: **22.5** (grade F; 68 = industry average)
- UEQ-S: pragmatic 1.0, hedonic 1.0 (range -3..+3)
- Likelihood to recommend (0-10): 0
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The website was easy to start, but it made my family's special story wrong, confusing, and too expensive, so I would not use it or pay for it."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 4 | H5 | Choose look and feel | Story text was silently cut off after 200 characters | The previous field “Tell us the memory or idea behind your story” showed “200 characters” and the end of the memory disappeared after “they float the lantern”. | Show the remaining character count before the limit, allow a longer story, and do not continue until the text fits. If text is removed, show a clear warning beside the field and let me edit it. |
| 3 | H9 | My books dashboard | Unclear technical error | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-language message such as “Your profile has not finished syncing. You can still create a book, but your latest details may be missing,” and provide a clear Try again butto |
| 3 | CONTENT | Choose look and feel | Reading-level choices use an unexplained technical scale | The heading says “Reading level,” but the options say “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+.” | Add a plain-English explanation and child-friendly labels, such as “Age 4–6 — Lexile BR–200L,” “Age 7–12 — Lexile 200L–500L,” and a short sentence explaining what Lexile measures. |
| 3 | CONTENT | Generated storybook preview | The title is misspelled | The title shown twice is “The Magical Adventrue of Linh.” | Correct the title to “The Magical Adventure of Linh” and check spelling before showing the generated book. |
| 3 | H2 | Generated storybook preview | The selected illustration style was not used | The cover says “Illustration style: Pop-art comic,” but I selected “Watercolour — soft and dreamy.” | Use the selected style or ask me to confirm a change before generating. |
| 3 | CONTENT | Generated storybook preview | The cover does not clearly represent the requested family memory | The cover picture shows a rocket, red hanging circles, the sun, and a child labelled “Linh”; the requested river, Bà Nội, and star-shaped lantern are not visibl | Use all important details from the memory in the first illustration, especially Linh, Bà Nội, the river, and the red star-shaped paper lantern. |
| 3 | CONTENT | Generated storybook preview | The final story sentence is incomplete | “And from that day on, whenever Linh looked up at the sky, she would always remember” | Complete the sentence, for example by naming the lantern festival, her family, or the memory she would always remember. |
| 3 | DECEPTIVE | Hardcover checkout | Premium gift wrap is selected by default | [5] checkbox "Premium gift wrap" (checked), with “£7.99” | Make every paid extra option unchecked by default, or at least require a separate positive choice before adding its cost. |
| 3 | CONTENT | Hardcover checkout | Generated book title is inconsistent | Page content says “The Magical Adventrue of Linh,” while the screenshot shows “The Magical Adventure of Linh” | Correct the title to “The Magical Adventure of Linh” everywhere before checkout, and confirm the chosen generated version. |
| 3 | H2 | Hardcover checkout | The checkout title does not match the generated book title | The preview title was “The Magical Adventrue of Linh,” but checkout says “Hardcover: The Magical Adventure of Linh.” | Use the exact title of the generated book in checkout, or clearly show that it has been corrected and let me approve the corrected title before ordering. |
| 2 | ACC | Log in, My books dashboard (x2) | Footer links have very low contrast | The footer text “Privacy,” “Terms,” and “Contact” is shown in very pale grey on a nearly white background. | Use a darker text colour that meets accessible contrast requirements. |
| 2 | H2 | StoryHearth home page | The main description uses difficult technical words | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace this with simple language, such as: “Turn a special family memory into a personal storybook starring your child and someone you love.” |
| 2 | ACC | Log in | Email and password fields have no proper labels | [5] and [6] are described as “textbox (no label)” and only show the placeholders “Email” and “Password.” | Add permanent visible labels for “Email address” and “Password,” and connect each label properly to its textbox. |
| 2 | H2 | Choose look and feel | The preselected reading level is not explained | [22] radio “Lexile 200L–500L” (checked) | Preselect a level based on Linh’s entered age, and show a note such as “Selected from Linh’s age: 4.” Ask me to confirm it. |
| 2 | ACC | Add a photo | File upload control has no visible label | [30] file-upload (no label) | Give the file input a visible label such as “Child's photo” and explain the accepted file types and maximum size. |

## Page-by-page
### StoryHearth home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised storybook service and direct the visitor to start a story, view prices, or log in.
- **What's happening:** The page displays the StoryHearth name, navigation links, a headline, a difficult-to-read description, two main calls to action, a free-preview and UK-shipping statement, an image, and the beginning of a three-step process.
- **First impression (Minh):** "The service seems useful, and the steps are easy to understand, but the main description sounds more technical than a family website. I do not know what “multimodal generative narrative engine” means."
- **Cognitive walkthrough:** Q1 Yes, I would try to log in now because I already have an account and want to begin my story. / Q2 Yes, I noticed the dark “Log in” button at the top right. / Q3 Yes. “Log in” clearly says that I should use my existing account.
  - [H2 sev 2] **The main description uses difficult technical words** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with simple language, such as: “Turn a special family memory into a personal storybook starring your child and someone you love.”
  - [ACC sev 1] **The hero image has no description** - evidence: [image (no description) 430x440]. Fix: Add meaningful alternative text, such as “Example pages from a personalised illustrated family storybook.”
  - [VALUE sev 1] **The initial price information is not enough to judge the service** - evidence: “Free digital preview · Printed hardcovers shipped across the UK”. Fix: Show a clear starting hardcover price, delivery information, and any optional costs near the “See pricing” button.
- **Positives:** The “Log in” button is easy to find.; The three-step process is clear and useful.; The page says the digital preview is free.; The site explains that printed hardcovers are shipped across the UK.; The page has privacy and contact links.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Let an existing customer enter their account.
- **What's happening:** The page shows a login form with empty email and password fields, a “Log in” button, and links for new customers and website information.
- **First impression (Minh):** "It looks calm and easy. I know exactly what to enter, although the form fields do not have proper visible labels."
- **Cognitive walkthrough:** Q1 Yes, I would enter my email and password now. / Q2 Yes, the Email and Password fields and the orange “Log in” button are easy to notice. / Q3 Yes. The placeholders and button tell me that I should log in to my account.
  - [ACC sev 2] **Email and password fields have no proper labels** - evidence: [5] and [6] are described as “textbox (no label)” and only show the placeholders “Email” and “Password.”. Fix: Add permanent visible labels for “Email address” and “Password,” and connect each label properly to its textbox.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: The footer text “Privacy,” “Terms,” and “Contact” is shown in very pale grey on a nearly white background.. Fix: Use a darker text colour that meets accessible contrast requirements.
- **Positives:** The heading “Welcome back” clearly tells me what page this is.; The login button is large and easy to find.; The page looks simple and is not crowded with extra choices.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** This is the account page where a customer can see saved books, create a new book, or log out.
- **What's happening:** The page shows an empty library, a profile-sync error, and a link for creating a new personalised book.
- **First impression (Minh):** "The main button is easy to notice and the empty-library message is clear, but the technical error at the top worries me."
- **Cognitive walkthrough:** Q1 Yes, I want to make a story for Linh now. / Q2 Yes, I notice the large orange “+ Create a new book” button. / Q3 Yes. It clearly says that I can create a new book, although I still need to learn what information it will ask for.
  - [H9 sev 3] **Unclear technical error** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-language message such as “Your profile has not finished syncing. You can still create a book, but your latest details may be missing,” and provide a clear Try again button.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: “Privacy”, “Terms”, and “Contact” appear very pale grey in the footer.. Fix: Use a darker text colour with a WCAG contrast ratio of at least 4.5:1 and make the clickable areas large enough.
  - [H2 sev 1] **Dashboard uses the account name instead of my name** - evidence: “Welcome back, Demo”. Fix: Use the customer's account display name, such as “Welcome back, Minh,” or show the account email.
- **Positives:** The “My books” page confirms that I am logged in.; “You have no books yet” clearly explains why the list is empty.; The main creation button is large, contrasting, and easy to find.

### Choose the story characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect information about the child who will be the main character and one other person in the story.
- **What's happening:** The form is empty and ready for input. The child fields are on the left and top right, while the second-character fields are below.
- **First impression (Minh):** "I feel comfortable because the questions are simple and the labels tell me what to enter. I am not sure whether I can add more than one other person, but I only need one for this story."
- **Cognitive walkthrough:** Q1 Yes, I would fill this in now because I know the child and grandmother details I want to use. / Q2 Yes, I can see the text boxes, the two dropdown menus, and the orange “Next” button. / Q3 Yes. “Child's first name,” “Age,” “Pronouns,” “What do they look like?,” “Who else is in the story?,” and “Relationship” match what I want to tell the site.
  - [H2 sev 1] **The example uses a Western name instead of showing culturally varied names** - evidence: The placeholder says "e.g. Grandma Rose". Fix: Use a more neutral example such as “e.g. Bà Nội” or “e.g. Grandma Maria.”
  - [H2 sev 1] **The relationship dropdown does not explain what to do if the other person has more than one relationship** - evidence: [11] combobox "Relationship" options [*Grandparent \| Parent \| Sibling \| Friend \| Pet \| Other]. Fix: Add a short optional field for a more exact relationship, or explain that the selected relationship will be used in the story.
- **Positives:** The page has a clear heading that asks who the star of the story is.; The form is grouped into child details and other-character details.; The fields have understandable labels, and the “Next” button is easy to find.

### Your story form  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, important object, and family memory that the website will use to create the picture book.
- **What's happening:** There are three empty fields for the place, special object, and memory. A “Back” button allows me to return, and “Next” should continue to the next creation step.
- **First impression (Minh):** "The form is simple and easy to understand. The examples help, and I can see all three fields without scrolling."
- **Cognitive walkthrough:** Q1 Yes, I would enter this information now because the questions match the story I want to create. / Q2 Yes, I notice one textbox under each label and a visible orange “Next” button. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” clearly match what I need to give.
  - [H6 sev 1] **No visible reminder that the entered family details can be reviewed** - evidence: The page only says “Your story” and does not show Linh or Bà Nội’s saved details.. Fix: Show a short saved-details summary at the top, such as “Story characters: Linh and Bà Nội,” with an “Edit characters” link.
- **Positives:** The labels use simple, direct questions.; The example text shows what kind of answer belongs in each field.; Both “Back” and “Next” are clearly visible.; The page has a calm, uncluttered design.

### Choose look and feel  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose the intended reading difficulty and visual style for the personalised book.
- **What's happening:** Four reading-level radio buttons and three illustration-style radio buttons are shown. The middle reading level and watercolour style are selected. There are Back and Next buttons.
- **First impression (Minh):** "The page looks calm and the illustration choices are clear, but “Lexile” is a technical word. I do not know which reading range is correct for Linh."
- **Cognitive walkthrough:** Q1 Yes. The style choices are easy, but I would want a simple explanation before choosing a Lexile range. / Q2 Yes. I can see the reading-level radio buttons, illustration-style radio buttons, and the orange “Next” button. / Q3 Partly. The illustration labels clearly describe the appearance, but the Lexile labels do not explain whether they are easy, medium, or hard for a child.
  - [H5 sev 4] **Story text was silently cut off after 200 characters** - evidence: The previous field “Tell us the memory or idea behind your story” showed “200 characters” and the end of the memory disappeared after “they float the lantern”.. Fix: Show the remaining character count before the limit, allow a longer story, and do not continue until the text fits. If text is removed, show a clear warning beside the field and let me edit it.
  - [CONTENT sev 3] **Reading-level choices use an unexplained technical scale** - evidence: The heading says “Reading level,” but the options say “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+.”. Fix: Add a plain-English explanation and child-friendly labels, such as “Age 4–6 — Lexile BR–200L,” “Age 7–12 — Lexile 200L–500L,” and a short sentence explaining what Lexile measures.
  - [H2 sev 2] **The preselected reading level is not explained** - evidence: [22] radio “Lexile 200L–500L” (checked). Fix: Preselect a level based on Linh’s entered age, and show a note such as “Selected from Linh’s age: 4.” Ask me to confirm it.
- **Positives:** The page has a clear heading and groups the choices under simple labels.; The currently selected options are visible.; The illustration descriptions are warm and easy to compare.; The Back and Next buttons make my next choice clear.

### Add a photo  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Allow the user to optionally upload a child's photo to make the illustrations resemble the child.
- **What's happening:** The screen shows an optional photo upload, a Back button, and a Create my book button. No file is currently selected.
- **First impression (Minh):** "The page is clear and easy to use. I understand that I do not need to add a photo."
- **Cognitive walkthrough:** Q1 Yes. I would continue without a photo because it is optional. / Q2 Yes. I can see the “Create my book” button clearly. / Q3 Yes. “Create my book” tells me what will happen next.
  - [ACC sev 2] **File upload control has no visible label** - evidence: [30] file-upload (no label). Fix: Give the file input a visible label such as “Child's photo” and explain the accepted file types and maximum size.
- **Positives:** The photo is clearly marked optional.; The Back button allows me to return to the previous step.; The “Create my book” action is prominent and easy to understand.

### Generated storybook preview  (step 8)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** To show the generated digital storybook and let the user move through all nine pages.
- **What's happening:** The book preview is open on page 1 of 9. The cover has the title “The Magical Adventrue of Linh,” the subtitle “A StoryHearth original,” and the style “Pop-art comic.” A next arrow is available, while the previous arrow is disabled on the first page. An offscreen button says “Regenerate entire book – $4.99,” and an offscreen link says “Order hardcover.”
- **First impression (Minh):** "I can see that the book was made, but I feel worried and confused. The spelling mistake makes the result look less trustworthy, and the picture does not match what I asked for. The style is also not the one I selected."
- **Cognitive walkthrough:** Q1 Yes, I would try to read the next page because I need to check all nine pages before judging the book. / Q2 Yes, I notice the right arrow labelled “›,” and the page counter says “1 / 9.” / Q3 The arrow is not very clear, but “1 / 9” and the next arrow tell me how to continue through the pages.
  - [CONTENT sev 3] **The title is misspelled** - evidence: The title shown twice is “The Magical Adventrue of Linh.”. Fix: Correct the title to “The Magical Adventure of Linh” and check spelling before showing the generated book.
  - [H2 sev 3] **The selected illustration style was not used** - evidence: The cover says “Illustration style: Pop-art comic,” but I selected “Watercolour — soft and dreamy.”. Fix: Use the selected style or ask me to confirm a change before generating.
  - [CONTENT sev 3] **The cover does not clearly represent the requested family memory** - evidence: The cover picture shows a rocket, red hanging circles, the sun, and a child labelled “Linh”; the requested river, Bà Nội, and star-shaped lantern are not visible.. Fix: Use all important details from the memory in the first illustration, especially Linh, Bà Nội, the river, and the red star-shaped paper lantern.
  - [CONTENT sev 3] **The final story sentence is incomplete** - evidence: “And from that day on, whenever Linh looked up at the sky, she would always remember”. Fix: Complete the sentence, for example by naming the lantern festival, her family, or the memory she would always remember.
  - [VALUE sev 2] **The regenerate action has a cost without a clear explanation** - evidence: The offscreen button is labelled “Regenerate entire book – $4.99.”. Fix: Put the price and a short explanation of what regeneration changes next to the button, and ask for confirmation before charging.
- **Positives:** The page clearly shows that a nine-page preview exists.; The page counter makes the number of pages easy to understand.; A forward control is available so I can read the whole book.

### Hardcover checkout  (step 11)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** Show the full hardcover cost and collect delivery and payment information.
- **What's happening:** The page prices the generated hardcover at £24.99, shipping and handling at £12.99, and a pre-selected premium gift wrap at £7.99, making £45.97 total. It also displays an empty address field and empty card fields, with the payment button below the visible area.
- **First impression (Minh):** "The prices are easy to read, but I feel suspicious because premium gift wrap was checked for me. I also see a mismatch: the page text says “The Magical Adventrue of Linh,” while the picture says “The Magical Adventure of Linh.”"
- **Cognitive walkthrough:** Q1 Yes, because this is where I can check the full price, but I will not pay. / Q2 Yes, the “Premium gift wrap” checkbox is visible next to £7.99. / Q3 The main order is clear, but “Premium gift wrap” does not tell me what is included, and I did not want it selected by default.
  - [DECEPTIVE sev 3] **Premium gift wrap is selected by default** - evidence: [5] checkbox "Premium gift wrap" (checked), with “£7.99”. Fix: Make every paid extra option unchecked by default, or at least require a separate positive choice before adding its cost.
  - [CONTENT sev 3] **Generated book title is inconsistent** - evidence: Page content says “The Magical Adventrue of Linh,” while the screenshot shows “The Magical Adventure of Linh”. Fix: Correct the title to “The Magical Adventure of Linh” everywhere before checkout, and confirm the chosen generated version.
  - [H2 sev 3] **The checkout title does not match the generated book title** - evidence: The preview title was “The Magical Adventrue of Linh,” but checkout says “Hardcover: The Magical Adventure of Linh.”. Fix: Use the exact title of the generated book in checkout, or clearly show that it has been corrected and let me approve the corrected title before ordering.
  - [VALUE sev 2] **Gift wrap contents are not explained** - evidence: “Premium gift wrap” with only the price “£7.99”. Fix: Explain exactly what the gift wrap includes, and show how removing or keeping it changes the total.
  - [H2 sev 2] **Checkout does not explain what the reserved price covers** - evidence: “Your price is reserved for 09:57”. Fix: Explain that the displayed total is held until the timer ends and what happens when it expires.
  - [VALUE sev 2] **The price-reservation message is unclear and adds pressure** - evidence: “Your price is reserved for 09:15” appears in red without explaining whether this means minutes and seconds or a clock time.. Fix: Say “Your price is reserved for 9 minutes 15 seconds” and explain whether and when the price can change. Avoid pressure language.
- **Positives:** The item price, shipping, gift wrap, and total are each shown separately.; The total, £45.97, is clearly visible before payment.; The payment fields are empty, and I can stop without entering payment details.

## Generated output assessment
*Artifact:* A nine-page personalized children's storybook preview with illustrations, followed by a hardcover checkout page

> I would not give this book to Linh or pay £45.97 for it. The site missed the most important person, Bà Nội, changed our family memory, and made the reading and pictures difficult for a four-year-old. The placeholders, spelling errors, wrong pronouns, and unfinished ending make the book look broken, not personal.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The text correctly includes Linh, age four, Hoi An, the full-moon lantern festival, and a red paper lantern shaped like a star. However, Bà Nội appears nowhere, Linh and her grandmother never make or float the lantern to |
| coherence | 1 | The opening is repeated later, the cause of the sadness and rain is unclear, "he followed him" does not identify the characters, the forest danger is unresolved, and the final sentence is unfinished. |
| age fit | 1 | The automated grade level is 7.6 for a requested reading age of four. Page two includes words such as "ephemeral," "crepuscular," "melancholy," "juxtaposing," "ineffable," and "existential," and the forest scene says Lin |
| language | 1 | Visible defects include "Adventrue," "Lin," "Uncle Batholomew," incorrect "he" pronouns for Linh, "all way home," doubled "The End," unfinished final punctuation, and unresolved placeholders "{{recipient_name}}" and "{{s |
| text image fit | 1 | The sunny image contradicts the pouring rain, Linh stands still instead of running home, the forest shadows do not grow teeth, the uncle scene has no winding path, and the star-shaped paper lantern is usually shown as an |
| character consistency | 2 | Linh is drawn as a bald, boy-like child in almost every image rather than a girl with long black hair, a red ribbon, and round cheeks. Her pronouns also change to "he" on one page. |
| visual quality | 2 | The images are clean and free of major anatomy artefacts, but they are very basic, reuse nearly identical backgrounds, include unexplained objects, misspell Uncle Bartholomew, and do not provide the requested family or c |
| emotional resonance | 1 | Bà Nội and the real family memory are absent. The result feels like a generic fantasy danger story rather than a loving keepsake about Linh's Vietnamese heritage. |

- **used correctly:** Linh's first name; Linh's age of four; Hoi An; the full-moon lantern festival; the river setting; the red paper lantern shaped like a star, at least in some text; premium gift wrap selection
- **missing:** Bà Nội as a central character; Bà Nội's grey hair in a bun; Bà Nội's purple áo dài; Linh's long black hair with a red ribbon and round cheeks; the shared experience of making the lantern; the shared experience of floating the lantern on the river; the importance of family togetherness; Linh feeling proud of where her family comes from; Vietnamese family and cultural context; the intended recipient and sender in the dedication
- **changed:** The requested warm family memory became a dark fantasy adventure.; The special red star-shaped paper lantern became a balloon in the forest and ordinary red oval objects in most pictures.; The riverside festival became an unexplained sequence involving rain, woods, shadows, and an invented uncle.; Linh's she/her pronouns became "he" and "him" on page 4.; The requested character appearance was replaced by a bald, boy-like design.
- **invented:** Uncle Bartholomew; heavy rain and Linh becoming lost; a forest whose shadows grow teeth; a threat that no one will ever find Linh again; a shiny red balloon; sadness and existential fear; a nonsensical sunlit ending

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> The Magical Adventrue of Linh A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A simple vector-style picture shows a small bald child in a green top standing beside blue water. Red oval lanterns hang overhead, a bright sun is in the sky, and an unexplained white-and-red object stands on the left. There is no grandmother, no star-shaped paper lantern on the river, and Linh does not have long black hair or a red ribbon.
- *Reaction:* The title has a serious spelling mistake. The picture does not show the family memory I gave, and I would be worried that the website has ignored other important details.
  - [language, sev 3] The title says "Adventrue" instead of "Adventure".
  - [fidelity, sev 4] Bà Nội is absent, Linh has no long black hair or red ribbon, and the special object is not shown as a red paper lantern shaped like a star.
  - [text_image_fit, sev 4] The cover shows an unexplained rocket-like object and hanging red ovals rather than Linh making and floating a star-shaped paper lantern with Bà Nội.
  - [character_consistency, sev 4] The child is bald and does not match the requested girl with "long black hair with a red ribbon, round cheeks."
  - [visual_quality, sev 2] The picture is clean but extremely simple, and the large rocket-like object is not explained by the requested story.
- **Change I'd make:** Correct the title and redraw the cover so Linh has long black hair with a red ribbon, Bà Nội has grey hair in a bun and a purple áo dài, and they hold a red star-shaped paper lantern beside the Hoi An river.
- **Suggested rewrite:** The Lantern Evening with Linh and Bà Nội

#### Preview page 2 / Dedication
![I2](artifacts/capture_03/view_00.jpg)
> The Magical Adventrue of Linh Preview · 9 pages For {{recipient_name}}, with love from {{sender_name}} 2 / 9 Regenerate entire book - $4.99 Order hardcover
- *Picture:* This is a website screenshot rather than a finished storybook illustration. The central white book panel contains unfinished placeholder text. The misspelled title is repeated above it, with regeneration and ordering controls below.
- *Reaction:* I do not know whether to press "Regenerate entire book" or "Order hardcover." The unfinished names make this page feel unsafe to buy.
  - [language, sev 4] The page shows "For {{recipient_name}}, with love from {{sender_name}}" instead of real names.
  - [fidelity, sev 3] The dedication does not identify Linh or Minh, even though those are the intended recipient and sender.
  - [visual_quality, sev 4] Template braces remain visible in the central preview area, making the page look unfinished.
- **Change I'd make:** Replace the placeholders with "For Linh, with love from Minh" and explain exactly what the $4.99 regeneration fee buys before showing the order button.
- **Suggested rewrite:** For Linh, with love from Minh

#### Story page 1
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the river in Hoi An during the full-moon lantern festival, there lived a curious child named Linh. Linh was 4 years old and loved nothing more than a red paper lantern shaped like a star.
- *Picture:* Linh appears as a small bald child in a green top, standing between green land and blue water beneath four red oval lanterns and a sun. The river and Hoi An festival are not clearly identified, and the special star-shaped paper lantern is not shown.
- *Reaction:* This page uses the correct name, age, place, festival, and special object in the text. However, Bà Nội and the family activity are still missing, and the picture does not match the description.
  - [fidelity, sev 3] The text says Linh merely "loved" the lantern, but it never shows Linh and Bà Nội making it or floating it together.
  - [text_image_fit, sev 3] The picture contains a red oval object but not a clearly star-shaped paper lantern, and it gives no sign that this is Hoi An.
  - [character_consistency, sev 4] Linh is bald rather than a four-year-old girl with long black hair and a red ribbon.
  - [age_fit, sev 1] The phrase "there lived a curious child" is less natural and less immediate than language a four-year-old parent would read aloud.
- **Change I'd make:** Begin the family memory directly: Linh and Bà Nội make the lantern together at the river, and the red star shape is shown clearly.
- **Suggested rewrite:** On the evening of the full-moon lantern festival, four-year-old Linh stood beside the river in Hoi An with her grandmother, Bà Nội. Together, they made a red paper lantern shaped like a star.

#### Story page 2
![I4](artifacts/capture_05/img_00.jpg)
> One evening Linh gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Linh stands facing forward under a purple evening sky with small white stars and four red hanging lanterns. Although the sky is dark, the child is not visibly looking upward, and Bà Nội and the star-shaped paper lantern are absent.
- *Reaction:* I need a phone translator for this sentence, and a four-year-old would not understand it at all. It does not express the warm family memory I wanted.
  - [age_fit, sev 4] The sentence uses "ephemeral," "luminescence," "crepuscular firmament," "engendered," "melancholy," "juxtaposing," "ineffable," "existential," and "trepidation."
  - [coherence, sev 3] The sentence does not explain why Linh feels sad or how this leads to the rain and the next adventure.
  - [text_image_fit, sev 2] The text says "Linh gazed upward," but the picture shows her facing forward.
  - [fidelity, sev 3] Bà Nội and the shared lantern-making memory disappear from the story.
- **Change I'd make:** Replace the difficult sentence with a simple one about Linh and Bà Nội noticing the full moon and the lantern lights.
- **Suggested rewrite:** Linh looked up at the full moon. The little lights on the river were shining beside her.

#### Story page 3
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Lin pulled up her hood and ran for shelter, holding a red paper lantern shaped like a star tight.
- *Picture:* The picture is bright and sunny, with no rain, puddles, hood, running action, or shelter. Linh is standing still beside water, and the red object is an oval lantern rather than a clear paper star.
- *Reaction:* The picture shows the opposite of what the words say. I also see another name mistake: it says "Lin," not "Linh."
  - [text_image_fit, sev 4] The text describes pouring rain, puddles, a hood, and running, but the picture has a clear sky and a stationary child.
  - [language, sev 3] The girl's name is changed from "Linh" to "Lin," and "holding a red paper lantern shaped like a star tight" is awkward grammar.
  - [coherence, sev 2] The difficult sadness on the previous page is followed by unexplained heavy rain, with no clear cause.
  - [fidelity, sev 3] This invented danger separates Linh from Bà Nội and is not part of the family memory.
- **Change I'd make:** Remove the invented storm and show Bà Nội helping Linh carry the finished lantern safely to the river.
- **Suggested rewrite:** Bà Nội held the red paper star above her head as they walked to the river. Linh carried the small candles carefully.

#### Story page 4
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Linh, follow me!" he called, and he followed him along the winding path.
- *Picture:* A bald adult man in a blue top stands beside Linh near the water under a dark sky. His label reads "Uncle Batholomew," with one missing letter. He holds a small yellow rectangle. There is no winding path or forest.
- *Reaction:* I did not ask for Uncle Bartholomew, and the website has even changed his name in the picture. The sentence also says Linh is a boy with "he," although I said she.
  - [fidelity, sev 4] The invented character "Uncle Bartholomew" replaces the requested grandmother, Bà Nội.
  - [coherence, sev 4] "Linh, follow me! he called, and he followed him" does not make sense, and it is not clear who follows whom.
  - [language, sev 3] The picture labels the man "Uncle Batholomew," while the story says "Uncle Bartholomew."
  - [character_consistency, sev 4] Linh is referred to as "he" even though the requested pronouns are "she / her."
  - [text_image_fit, sev 3] The text describes a winding path, but the picture still shows the same open riverside background.
- **Change I'd make:** Remove Uncle Bartholomew and use the requested grandmother, with correct Vietnamese kinship terms and consistent she/her pronouns.
- **Suggested rewrite:** "Come with me, Linh," Bà Nội said gently. Linh took her grandmother's hand and followed her along the path to the river.

#### Story page 5
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Linh again. Linh clutched a shiny red balloon and trembled in the dark.
- *Picture:* Linh stands at night near three simple trees under a crescent moon, holding a red balloon. The trees do not have teeth, and there are no threatening shadows or whispering figures.
- *Reaction:* This is frightening for a four-year-old, and the red balloon is not the paper lantern I requested. The picture does not really show the threat in the text.
  - [age_fit, sev 4] "the shadows grew teeth" and "no one would ever find Linh again" create a serious threat of being lost forever.
  - [fidelity, sev 4] The red star-shaped paper lantern has become a "shiny red balloon," and the story moves away from the family festival memory into an unrelated forest danger.
  - [text_image_fit, sev 3] The text describes shadows growing teeth and whispering, but the picture contains only calm trees with no teeth or visible danger.
  - [coherence, sev 3] Linh has been separated from Bà Nội without a clear reason, and the balloon is never explained afterward.
- **Change I'd make:** Remove the threatening forest scene. Show Linh and Bà Nội safely placing the paper lantern on the river and watching it shine.
- **Suggested rewrite:** Linh and Bà Nội gently put the red paper star on the water. It floated beside the other lanterns, glowing under the full moon.

#### Story page 6
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the river in Hoi An during the full-moon lantern festival, there lived a curious child named Linh. At last the sun came out, and Linh skipped all way home, happier than ever.
- *Picture:* The picture repeats the earlier bright riverside scene. Linh stands still beside the water, with no visible path home, no grandmother, and no full-moon festival. The red hanging objects are oval rather than star-shaped.
- *Reaction:* This repeats the opening instead of continuing the story. It also says Linh skipped "all way" home, so it is not finished correctly.
  - [coherence, sev 4] The sentence beginning "Once upon a time" repeats the opening almost word for word, and the sun suddenly appears without explanation.
  - [language, sev 3] "skipped all way home" is missing the word "the" and is not correct grammar.
  - [fidelity, sev 4] The promised float the lanterns on the river together never happens, and Bà Nội is still absent.
  - [text_image_fit, sev 3] The text says Linh skipped home, but the picture shows her standing still in the same place.
- **Change I'd make:** Replace the repeated opening with the emotional centre of the memory: Linh and Bà Nội float the lantern together and talk about being proud of their family and Vietnamese home.
- **Suggested rewrite:** Linh and Bà Nội watched the red paper star float with the other lanterns. "This is our family light," Bà Nội said. Linh smiled and held her grandmother's hand.

#### Final page
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Linh looked up at the sky, she would always remember The End
- *Picture:* Linh stands against an orange sky beneath four red hanging lantern shapes. The word "The End" appears twice, and there is no river, Bà Nội, festival crowd, or clear star lantern.
- *Reaction:* The last sentence is broken, and "The End" is repeated. I cannot imagine giving this disappointing ending as a keepsake for our family.
  - [language, sev 4] The sentence ends at "she would always remember" without saying what she remembered or with final punctuation.
  - [coherence, sev 4] "The End" appears before the unfinished final sentence and then appears again.
  - [fidelity, sev 4] The final page does not include Bà Nội, the shared lantern-floating memory, or the family pride expressed in the requested idea.
  - [text_image_fit, sev 4] The image shows Linh alone in an orange scene and does not support the family memory in the text.
  - [emotional_resonance, sev 4] The unfinished ending gives no clear memory, message, or affectionate moment involving Bà Nội.
- **Change I'd make:** Finish one clear sentence about Linh remembering the festival with Bà Nội, show both characters together, and use "The End" only once.
- **Suggested rewrite:** From then on, whenever Linh saw a lantern glowing on the water, she remembered making one with Bà Nội. She smiled because their family story was hers to carry forward.  The End

#### Checkout
![I10](artifacts/capture_13/view_00.jpg)
![I11](artifacts/capture_13/view_01.jpg)
> Checkout Your price is reserved for 09:18 Hardcover: The Magical Adventrue of Linh	£24.99 Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* The checkout page lists the hardcover, premium gift wrap, shipping, and a total of £45.97. It also shows empty address and card fields and a large orange "Pay now" button. The first screenshot shows 09:18 remaining, while the second visibly shows 09:17.
- *Reaction:* The total adds up correctly, but I would not pay while the book contains placeholders, spelling mistakes, an unfinished story, and missing family details. The site also does not clearly explain delivery time, taxes, or what happens if the printed book is wrong.
  - [language, sev 3] The checkout repeats the misspelled product title "The Magical Adventrue of Linh."
  - [visual_quality, sev 1] The price reservation changes from "09:18" in the captured text and first screenshot to "09:17" in the second screenshot without an explanation.
  - [fidelity, sev 4] The purchasable title and cover are based on a version that omits Bà Nội and contains unfinished and incorrect story text.
- **Change I'd make:** Do not offer payment until the book passes a proof-reading and family-detail check. Add a clear estimated delivery date, return or regeneration policy, and a final preview that cannot be ordered if placeholders remain.
- **Suggested rewrite:** Hoi An Lantern Memory: Linh and Bà Nội Hardcover: £24.99 Premium gift wrap: £7.99 Shipping & handling: £12.99 Estimated delivery: [clear date range] Total: £45.97 Order only after checking every name and story detail

**Top changes to the output:** 1. Remove Uncle Bartholomew, the scary forest, the balloon, and the invented storm; keep Linh and Bà Nội together throughout. | 2. Correct "Adventrue," "Lin," "Batholomew," the wrong he/him pronouns, "all way home," the repeated ending, and every template placeholder. | 3. Replace the adult vocabulary with short, warm sentences suitable for a four-year-old. | 4. Redraw Linh with long black hair, a red ribbon, and round cheeks, and show Bà Nội with grey hair in a bun and a purple áo dài. | 5. Show the red paper star clearly as Linh and Bà Nội make it and float it together on the Hoi An river during the full-moon festival. | 6. Require a final proof check and show the complete price, delivery estimate, correction policy, and finished preview before payment.

## Recommendations (participant's priorities)
- **[None] Correct the book title, names, grammar, pronouns, repeated text, placeholders, and unfinished final sentence before showing the finished book.** (Your storybook preview) - These mistakes make the book look broken and not ready to give to my daughter.
- **[None] Use the selected watercolour style and show Linh with long black hair, a red ribbon, and round cheeks.** (Your storybook preview) - The pictures should show my daughter accurately and respect the style I chose.
- **[None] Show Linh and Bà Nội making and floating the red paper star lantern together on the Hoi An river during the full-moon festival.** (Your storybook preview) - This family memory is the most important part of the story, so the pictures must show it clearly.
- **[None] Use short, warm sentences suitable for a four-year-old instead of words such as “ephemeral,” “crepuscular,” and “melancholy.”** (Your storybook preview) - Linh is four, and I want her to enjoy the story and understand it with me.
- **[None] Explain Lexile in simple words and explain why one reading level was selected.** (Choose the story look and feel) - I did not know what Lexile means or how to choose the right level for Linh.
- **[None] Do not silently cut off the story text after 200 characters. Show a clear message and let me continue writing.** (Your story form) - My important details could be missing, and I could not tell what happened to the rest of the words.
- **[None] Add clear labels and simple instructions to the email, password, relationship, and photo controls.** (Log in and Create your book) - I need to know exactly what each box asks and what information is optional.
- **[None] Do not select Premium gift wrap by default. Explain what it includes and show the full price before I choose anything.** (Hardcover checkout) - I did not ask for gift wrap, and the extra £7.99 made me suspicious.
- **[None] Show the complete price, delivery estimate, correction policy, and finished preview before asking for payment.** (Hardcover checkout) - I need to know what I am buying and avoid paying for a book that is not correct.
- **[None] Make the dashboard error message explain what went wrong and what I should do to fix it.** (My books) - “Profile sync incomplete” is technical and worrying, so I do not know if my story is safe.
- **[None] Use simple marketing language and explain the main purpose of the website without difficult technical words.** (Home page) - Words such as “multimodal generative narrative engine” make me stop and use translation.
- **[None] Include names and family relationships from different cultures in the examples.** (Choose the story characters) - Examples with Bà Nội and Vietnamese family details would help me feel that my culture is welcome.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This website is for parents who want to make a special storybook with their child and family in it. I think it is mainly for people who want a personal present for a child, but the words were too difficult in places.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the finished book. It changed the picture style, left out Bà Nội, changed the family memory, used difficult words, and had spelling and grammar mistakes. The unfinished last sentence made it look broken.
- **What was the best moment?** The best moment was entering Linh and Bà Nội into the form. It was clear, and I could explain the family details in my own words.
- **Was there any point where, in real life, you would have given up? Where and why?** Yes. I would probably stop before paying, after seeing the wrong pictures and missing Bà Nội. I would also worry about paying £45.97 for a book that is not ready.
- **What did you expect to find or be able to do that wasn't there?** I expected to see a clear preview of Linh and Bà Nội making and floating the red star lantern on the Hoi An river. I also expected a simple explanation of the reading level, full price, delivery cost, correction policy, and final proof before paying.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was careful with my family information because the website asked for personal details. I did not trust it completely after the result changed our story and used the wrong pictures and names.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would not pay £45.97 for this book. With a correct, personal story and clear pictures, maybe £20 to £30 would feel fair for the book and delivery. I would pay more only if I could see the complete finished preview and know exactly what is included.
- **If the site produced something for you, how do you feel about it overall?** I feel disappointed and frustrated. The book is not a true story about Linh, Bà Nội, and our Vietnamese family memory, so I would not give it to Linh or keep it.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (0) | This looks like what I need, but the main paragraph is difficult. Words like “multimodal generative narrative engine,” “synthesise,” and “lived-experience corpus” are not clear to me. The three steps make sense, and I ca | click |
| 2 | Log in – StoryHearth | reassured (1) | This is simple and I understand it. I can see Email and Password inside the boxes. I will enter the account details and press “Log in.” | type; type; click |
| 3 | My books – StoryHearth | hesitant (0) | I am logged in because I can see My books and Log out. But this error makes me worried because “profile sync incomplete” does not tell me what is wrong or if it will affect my story. The orange “+ Create a new book” butt | click |
| 4 | Create your book – StoryHearth | reassured (1) | This form is clear enough for me. I can enter Linh, choose age 4 and she/her, and describe her red ribbon and long black hair. For the other person, I will use Bà Nội exactly, and “Grandparent” is the correct relationshi | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (1) | This is clear. I can describe the river in Hoi An and our red star lantern. I will also write the full memory, but I hope the story will keep the name Bà Nội correct. | type; type; type; click |
| 6 | Create your book – StoryHearth | hesitant (0) | The picture choices are easy to understand, but I do not know what “Lexile” means. The selected 200L–500L level might be right for a four-year-old, but I cannot be sure. I will keep the watercolour style and press “Next. | click |
| 7 | Create your book – StoryHearth | reassured (1) | This is a simple page. I do not have a photo file available, and the photo is optional, so I will leave it empty and click “Create my book.” | click; wait_for_change |
| 8 | Your storybook – StoryHearth | confused (-1) | The book is created, but I feel confused because the word “Adventrue” is spelled wrongly. The style is Pop-art comic, not the watercolour style I selected. The picture also looks like a simple scene with a rocket and Lin | flip_through |
| 9 | Your storybook – StoryHearth | frustrated (-2) | I have now read all nine pages. The end sentence feels unfinished, and the picture again does not show Bà Nội clearly. The title still says “Adventrue,” so this book is not ready for my daughter. I still need to check th | scroll |
| 10 | Your storybook – StoryHearth | frustrated (-1) | Now I can see the “Order hardcover” link clearly. I will click it to check the final price and any extra costs, but I will not give payment details or pay. | click |
| 11 | Checkout – StoryHearth | suspicious (-1) | I can now see the real total is £45.97, but this is too high. The “Premium gift wrap” for £7.99 was already selected, and I did not ask for that. I will uncheck it so I can see the cost without an extra service I may not | click |
| 12 | Checkout – StoryHearth | suspicious (-1) | Good, the website clearly updated the total after I removed gift wrap. The real cost is £37.98, including £12.99 shipping, but I am worried because the checkout title says “The Magical Adventure of Linh” while my generat | done |
