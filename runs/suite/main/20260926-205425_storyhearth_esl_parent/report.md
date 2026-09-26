# UserQA report: Minh Tran on http://127.0.0.1:8765/

*Persona:* **Minh Tran** (33) - Recently-arrived parent reading English as a second language (CEFR B1).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 17 steps | *Pages reviewed:* 11 | *Issues:* 37 | *LLM calls:* 22 | *Wall time:* 398.1 s

## What the agent understood the website to be
- **what it is:** A website for creating personalised illustrated family storybooks.
- **who it is for:** Families who want to turn family memories into stories for children or relatives.
- **value proposition:** It can create a storybook preview from a child, another family member, a memory, a place, and a treasured object.
- **pricing model:** A free digital preview is mentioned. Printed hardcovers are available, but the price is not shown here; a Pricing link is available.
- **fit for me:** This fits my goal because I want a story for my daughter Linh featuring our family and the lantern festival in Hoi An. I need the steps and price to be easy to understand.
- **main tasks:** Log in, Describe family members, Share a family memory, Create and read a story preview, Find the price of a printed hardcover

## Scores
- SUS: **20.0** (grade F; 68 = industry average)
- UEQ-S: pragmatic 0.75, hedonic -0.75 (range -3..+3)
- Likelihood to recommend (0-10): 0
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The website helped me enter our memory, but the result changed our family story, so I would not use or recommend it yet."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Unclear error message | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain explanation, such as “Some profile information has not finished loading. You can still create a book, or refresh and try again,” and include a clear action if a fix is ne |
| 3 | H5 | Reading level and illustration style | The story text was silently cut to 200 characters | The previous action reported that the story box “now only shows 200 characters; the end of what you typed was cut off” | Show the character limit before typing, keep the full text internally, and ask for confirmation before continuing if any content was removed. |
| 3 | H1 | Book creation loading page | The loading screen does not explain the current step | The page shows only a circular loading symbol, with no text explaining that the book is being generated. | Show a clear message such as “Creating Linh’s storybook. This may take about a minute” and include a visible loading label for screen readers. |
| 3 | CONTENT | Generated storybook preview | The book title contains a spelling error | The title is shown as “The Magical Adventrue of Linh”. | Spell the word as “Adventure” in the title and check the cover and all page headings for spelling. |
| 3 | H2 | Generated storybook preview | The generated art style does not match my selection | The page says “Illustration style: Pop-art comic,” although I chose the watercolour pictures. | Save the selected watercolour style with the book, generate using that setting, and display the requested style beside the result. |
| 3 | CONTENT | Generated storybook preview | The cover does not reflect the personal details I entered | The cover shows a simple figure labelled “Linh,” with short/no visible long black hair or red ribbon, alongside a rocket and hanging red oval lights; the previe | Use the entered appearance details in the cover prompt and show Linh, Bà Nội, and the red star-shaped lantern in a watercolour Hoi An setting. |
| 3 | CONTENT | Generated storybook preview | The final sentence is incomplete | “And from that day on, whenever Linh looked up at the sky, she would always remember” | Check that the generated text is complete before showing the book, and warn me or let me edit the unfinished sentence. |
| 3 | CONTENT | Generated storybook preview | Important family and cultural details are missing from the final page | The final picture shows Linh and a simple rocket-like object, but not the red star-shaped paper lantern or Bà Nội. | Keep the entered names, object, people, and place in the generated story, and show a clear way to correct missing details before ordering. |
| 3 | VALUE | Simple pricing | Possible extra charges are not explained | "Hardcover book $24.99" and "20 glossy pages, printed and bound to last." | Show the currency clearly and state whether the price includes tax and shipping. If extra charges may apply, say so before checkout and give a clear example. |
| 3 | H2 | Simple pricing | The advertised page count does not match my book | The hardcover says "20 glossy pages," but my generated online book has 9 pages. | Explain how the 9-page story becomes 20 printed pages, or advertise the page count that matches the selected book. |
| 3 | DECEPTIVE | Checkout | Gift wrap is selected by default | checkbox "Premium gift wrap" (checked), £7.99 | Make every optional extra unchecked by default and label it clearly as an optional add-on. Show how the total changes when it is selected or removed. |
| 2 | ACC | Book creation loading page, Simple pricing, Log in (x3) | The footer text has very low contrast | “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” are extremely faint against the background. | Use darker, WCAG-compliant text contrast and make the clickable areas large enough. |
| 2 | H2 | StoryHearth home page | Difficult marketing language | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Use simple wording, for example: “We turn your family memories into a special illustrated storybook for your child.” |
| 2 | H9 | Log in | No visible way to recover a forgotten password | The page shows “Log in” and “Create an account”, but no “Forgot password?” link. | Add a clearly visible “Forgot password?” link below the password field. |
| 2 | H1 | My books dashboard | The warning gives no recovery steps | “Error 0x80070057: profile sync incomplete.” | Show whether the account is ready, and provide a “Try again” or “Refresh profile” button when appropriate. |

## Page-by-page
### StoryHearth home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** To explain the personalised family storybook service and direct me toward creating a story or viewing prices.
- **What's happening:** The home page shows the service description, two main action buttons, a three-step process, customer quotes, and footer links. The page has not started creating a story yet.
- **First impression (Minh):** "The three steps look useful, and I can see that a free digital preview is offered. However, the main description uses difficult words such as “multimodal generative narrative engine,” “synthesise,” “bespoke,” and “corpus,” so I do not fully understand it."
- **Cognitive walkthrough:** Q1 Yes. I want to create a story about Linh and Bà Nội, so I would look for the way to start or log in. / Q2 Yes. I notice the “Log in” link at the top right and the “Proceed” button. / Q3 “Log in” clearly matches the next step for using my account. “Proceed” is less clear because it does not say whether it starts a new story or continues one.
  - [H2 sev 2] **Difficult marketing language** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Use simple wording, for example: “We turn your family memories into a special illustrated storybook for your child.”
  - [H2 sev 1] **“Proceed” does not explain the result** - evidence: [5] link "Proceed →". Fix: Rename the button “Start your story” and explain that the next step is a free form and does not require payment.
  - [ACC sev 1] **The image has no description** - evidence: [image (no description) 430x440]. Fix: Add a useful alternative description, such as “An example family storybook with an adult and child reading together.”
- **Positives:** The page has a clear “Log in” link.; The three-step explanation uses simple headings: “Tell us who,” “Share a memory,” and “We write & illustrate.”; It clearly says “Free digital preview.”; The Pricing link is easy to find.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** This page lets an existing customer sign in with an email address and password.
- **What's happening:** The empty email and password fields and the orange “Log in” button are shown in the centre of the page. A “Create an account” link appears for new customers.
- **First impression (Minh):** "It looks calm, simple, and easy to understand. The form itself makes my next step clear."
- **Cognitive walkthrough:** Q1 Yes, I would enter my account details and log in now. / Q2 Yes, I immediately noticed the two fields and the large orange button. / Q3 Yes. The placeholders say “Email” and “Password”, and the button says “Log in”.
  - [H9 sev 2] **No visible way to recover a forgotten password** - evidence: The page shows “Log in” and “Create an account”, but no “Forgot password?” link.. Fix: Add a clearly visible “Forgot password?” link below the password field.
  - [ACC sev 1] **Footer links have very low contrast** - evidence: The bottom links “Privacy”, “Terms”, and “Contact” are very faint against the background.. Fix: Use darker text or stronger contrast for footer links.
- **Positives:** The form is short and easy to scan.; The button is large and clearly named.; The “Welcome back” heading tells me this is for returning customers.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** This page shows the books saved in my account and lets me start creating a new personalised book.
- **What's happening:** The page shows an empty account with no books. It provides a button to create a new book, and it displays a profile sync warning.
- **First impression (Minh):** "The main button is easy to find and I understand that I can make a new book. However, the error message at the top makes me worried and does not tell me whether my information is safe."
- **Cognitive walkthrough:** Q1 Yes, I would try to create a new book because that is what I came here to do. / Q2 Yes, I noticed the orange “+ Create a new book” button. / Q3 Yes, “Create a new book” clearly matches what I want to do.
  - [H9 sev 3] **Unclear error message** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain explanation, such as “Some profile information has not finished loading. You can still create a book, or refresh and try again,” and include a clear action if a fix is needed.
  - [H1 sev 2] **The warning gives no recovery steps** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Show whether the account is ready, and provide a “Try again” or “Refresh profile” button when appropriate.
- **Positives:** The “+ Create a new book” button is prominent and easy to understand.; The page clearly tells me that there are no books yet.; I can see that I am logged in because the page says “Welcome back, Demo” and offers “Log out.”

### Create your book – character details  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect details about the child who will be the hero and another person who will appear in the story.
- **What's happening:** The form is empty. It has fields for the child's first name, age, pronouns and appearance, followed by fields for another character's name and relationship. “Grandparent” is already selected, and the orange “Next” button continues the process.
- **First impression (Minh):** "The layout is clear and not crowded. I can easily match each box to what I know about Linh and Bà Nội."
- **Cognitive walkthrough:** Q1 Yes, I would enter the family details now. / Q2 Yes, the labelled text boxes, drop-down lists and orange “Next” button are easy to notice. / Q3 Yes. “Who’s the star of the story?” matches making Linh the hero, and “Who else is in the story?” lets me add Bà Nội. The label asks only for a first name, but I still have the full cultural name “Bà Nội.”
  - [H5 sev 2] **No field for the second person's appearance** - evidence: [9] “What do they look like? (optional)” appears only beneath the child's section, while [10] asks “Who else is in the story?” with no appearance field.. Fix: Add an optional “What do they look like?” field under the second-character details, with the same label and help as the child's appearance field.
  - [H2 sev 2] **The character name label may restrict Vietnamese names** - evidence: [10] “Who else is in the story?” and its placeholder says “e.g. Grandma Rose,” with no indication that a full or culturally meaningful name is welcome.. Fix: Rename the field to “Character's name” and use a culturally neutral example such as “e.g. Bà Nội or Grandma Rose.”
- **Positives:** The heading clearly says Linh will be the star.; The age and pronoun choices include age 4 and “she / her.”; The “Next” button has a clear, simple label.; The form avoids technical instructions and asks only for relevant details.

### Your story details  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect details about the setting, special object, and family memory for the personalised storybook.
- **What's happening:** The page presents three empty fields for the story place, special object, and memory, with navigation to the previous or next step.
- **First impression (Minh):** "This looks simple and calm. The questions tell me exactly what information to give, and I understand the example text."
- **Cognitive walkthrough:** Q1 Yes, I can explain this family memory in my own words. / Q2 Yes, I notice three large text boxes and a clearly visible Next button. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” match the details I want to include.
  - [CONTENT sev 1] **Grandmother's relationship is not requested** - evidence: The previous step only showed [10] “Who else is in the story?” and the current memory box is the only place to explain her role.. Fix: Add a relationship selector or example, such as “Who is the other person? Bà Nội (grandmother).”
- **Positives:** The three labels are direct and easy to understand.; The example placeholders explain what kind of answer is wanted.; Back and Next make it clear that this is a step-by-step form.; There is enough writing space for the full family memory.

### Reading level and illustration style  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose how easy the finished story should be to read and what the illustrations should look like.
- **What's happening:** The page shows four reading-level choices and three illustration styles. One reading level and one illustration style are selected, with Back and Next buttons below.
- **First impression (Minh):** "The page looks calm and the choices are easy to see. However, “Lexile” is a technical reading term that I do not understand."
- **Cognitive walkthrough:** Q1 Yes, because Linh is four and I want a story that will be easy for her age. / Q2 Yes, I notice the four reading-level radio buttons and the three illustration-style radio buttons. / Q3 Only partly. The illustration labels clearly describe the look, but the Lexile numbers do not clearly tell me which level is right for a four-year-old.
  - [H5 sev 3] **The story text was silently cut to 200 characters** - evidence: The previous action reported that the story box “now only shows 200 characters; the end of what you typed was cut off”. Fix: Show the character limit before typing, keep the full text internally, and ask for confirmation before continuing if any content was removed.
  - [H2 sev 2] **Reading levels use an unexplained technical scale** - evidence: “Reading level” followed by “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+”. Fix: Show plain-language labels such as “For ages 0–4 (beginning reader)” and put the Lexile score in smaller supporting text.
  - [H6 sev 2] **Age four is not matched clearly** - evidence: “Lexile 200L–500L” is checked by default, even though the supplied child age is 4.. Fix: Recommend the age-four level automatically and explain why, while still allowing me to change it.
- **Positives:** The page has one clear purpose: choosing the reading level and illustration style.; The selected radio buttons are visually clear.; The illustration descriptions are easy to understand.; There are clear “Back” and “Next” buttons.

### Add a photo  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Offer an optional child photo before generating the personalised book.
- **What's happening:** I can upload an image of Linh, go back to the previous step, or create the book without a photo.
- **First impression (Minh):** "This is clear and easy. It is good that the photo is optional."
- **Cognitive walkthrough:** Q1 I do not need to upload a photo because I do not have one ready and it is optional. / Q2 Yes, I can see the Choose file control and the Create my book button. / Q3 Yes, “Create my book” clearly matches what I want to do next.
  - [ACC sev 2] **Photo upload has no visible label** - evidence: [30] file-upload (no label) shows only “Choose file” and “No file chosen”.. Fix: Give the file input a visible label such as “Photo of Linh” and describe accepted formats and maximum file size.
  - [TRUST sev 2] **Photo privacy and retention are not explained here** - evidence: “Upload a clear photo of your child's face” does not say how the photo will be stored, used, or deleted.. Fix: Add a short privacy note beside the upload explaining whether the original photo is retained, whether it is used for training, and how to request deletion.
- **Positives:** The photo is clearly marked optional, so I can continue without one.; The explanation directly says what kind of photo to choose.; The Back and Create my book buttons make the next choices visible.

### Book creation loading page  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** To show that the new personalised storybook is being generated after the parent presses “Create my book.”
- **What's happening:** The form has disappeared and the page is waiting for the book to be generated. A circular loading symbol is shown, but there is no explanatory text, progress information, cancel control, or error message.
- **First impression (Minh):** "I can see that the website is doing something, but the empty box and spinner make me nervous. A simple message like “Creating Linh’s story. This may take one minute” would help me understand."
- **Cognitive walkthrough:** Q1 I would wait for a little while because the spinner suggests the website is working, but I would not wait forever without more information. / Q2 I notice the loading symbol, but I do not see any control for what to do next. / Q3 The loading symbol is not a label. Nothing explains whether my book was created or what stage it has reached.
  - [H1 sev 3] **The loading screen does not explain the current step** - evidence: The page shows only a circular loading symbol, with no text explaining that the book is being generated.. Fix: Show a clear message such as “Creating Linh’s storybook. This may take about a minute” and include a visible loading label for screen readers.
  - [H3 sev 2] **There is no way to stop or leave the generation safely** - evidence: No “Cancel,” “Wait,” or “My books” control is visible in the main content area; only the general [4] “My books” link is present.. Fix: Add a clear “Cancel” or “Continue in background” control and keep “My books” available without losing the book being created.
  - [ACC sev 2] **The footer text has very low contrast** - evidence: “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” are extremely faint against the background.. Fix: Use darker, WCAG-compliant text contrast and make the clickable areas large enough.
- **Positives:** The loading symbol is centred, so I can see that the website is working on the book.; The navigation still shows “My books,” which gives me one possible way to check my account.

### Generated storybook preview  (step 9)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** To preview the newly generated personalised storybook, move between its pages, and find options to regenerate or order it.
- **What's happening:** The first of nine story pages is displayed. The cover is titled “The Magical Adventrue of Linh,” identifies the art as pop-art comic, and has previous/next controls. Regeneration and hardcover-order controls are farther down the page.
- **First impression (Minh):** "I can see that a book has been created, but the spelling error and mismatch with the style I chose make me worried about the other cultural details."
- **Cognitive walkthrough:** Q1 Yes, I would read through the pages now to check the names, setting, characters, and objects. / Q2 Yes, the next-page button is visible, although it has only the symbol “›” and no text. / Q3 Partly. The arrow is understandable, but “Next page” would be clearer.
  - [CONTENT sev 3] **The book title contains a spelling error** - evidence: The title is shown as “The Magical Adventrue of Linh”.. Fix: Spell the word as “Adventure” in the title and check the cover and all page headings for spelling.
  - [H2 sev 3] **The generated art style does not match my selection** - evidence: The page says “Illustration style: Pop-art comic,” although I chose the watercolour pictures.. Fix: Save the selected watercolour style with the book, generate using that setting, and display the requested style beside the result.
  - [CONTENT sev 3] **The cover does not reflect the personal details I entered** - evidence: The cover shows a simple figure labelled “Linh,” with short/no visible long black hair or red ribbon, alongside a rocket and hanging red oval lights; the preview caption says “Pop-art comic.”. Fix: Use the entered appearance details in the cover prompt and show Linh, Bà Nội, and the red star-shaped lantern in a watercolour Hoi An setting.
  - [CONTENT sev 3] **The final sentence is incomplete** - evidence: “And from that day on, whenever Linh looked up at the sky, she would always remember”. Fix: Check that the generated text is complete before showing the book, and warn me or let me edit the unfinished sentence.
  - [CONTENT sev 3] **Important family and cultural details are missing from the final page** - evidence: The final picture shows Linh and a simple rocket-like object, but not the red star-shaped paper lantern or Bà Nội.. Fix: Keep the entered names, object, people, and place in the generated story, and show a clear way to correct missing details before ordering.
  - [ACC sev 2] **The next-page control has no text label** - evidence: [7] is shown only as a button labelled “›”.. Fix: Give the button an accessible name such as “Next story page,” and show visible text “Next” beside the arrow.
  - [H1 sev 2] **Completion was not clearly confirmed** - evidence: The previous screen had only a loading circle, and this screen does not say “Your book is ready” or clearly state that it was saved to My books.. Fix: After generation, show a clear confirmation such as “Your 9-page book is ready and saved to My books.”
  - [VALUE sev 2] **Hardcover price is hidden behind checkout** - evidence: [9] link "Order hardcover" appears beside “Regenerate entire book – $4.99,” with no hardcover amount shown.. Fix: Show the current hardcover price next to “Order hardcover,” including any shipping or other required charges.
- **Positives:** The page clearly shows that a 9-page book now exists.; The previous and next page controls are large and easy to see.; The cover title includes Linh’s correct name.

### Simple pricing  (step 12)
`http://127.0.0.1:8765/pricing.html`

![screenshot](screenshots/step_12.jpg)
- **Purpose:** Show the cost of the digital preview, hardcover book, and a new generated version.
- **What's happening:** Three pricing cards show Free, $24.99, and $4.99. A “Start your book” button appears below, but there is no control to choose or order the hardcover from this page.
- **First impression (Minh):** "The main prices are easy to read, and $24.99 is better than finding it only at checkout. However, the 20-page description does not explain why my generated book has only 9 pages, and I cannot tell what the final delivered price will be."
- **Cognitive walkthrough:** Q1 I would try to return to my book and find an order option, but I would not order from this pricing page because it has no book selector. / Q2 I notice the “Hardcover book” price card, but I do not notice a clickable order button for it. The only button says “Start your book.” / Q3 “Hardcover book” tells me the product type and its $24.99 base price, but it does not clearly say whether this is the total I will pay for my existing book.
  - [VALUE sev 3] **Possible extra charges are not explained** - evidence: "Hardcover book $24.99" and "20 glossy pages, printed and bound to last.". Fix: Show the currency clearly and state whether the price includes tax and shipping. If extra charges may apply, say so before checkout and give a clear example.
  - [H2 sev 3] **The advertised page count does not match my book** - evidence: The hardcover says "20 glossy pages," but my generated online book has 9 pages.. Fix: Explain how the 9-page story becomes 20 printed pages, or advertise the page count that matches the selected book.
  - [H7 sev 2] **No way to order the current book from pricing** - evidence: The only button is [6] "Start your book"; the "Hardcover book" card is not a control.. Fix: Add an “Order this book” button for each existing book, or direct me to the current book’s order page.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: The footer labels "Privacy," "Terms," and "Contact" appear very pale against the background.. Fix: Use darker text and a clearly visible focus or hover state that meets accessible contrast requirements.
- **Positives:** The heading “Simple pricing” and the large prices are easy to scan.; The $24.99 hardcover price is visible before checkout.; The $4.99 cost of generating a different story is shown clearly.; The page design is calm and not crowded.

### Checkout  (step 16)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_16.jpg)
- **Purpose:** Review the hardcover order price, delivery cost, and any extras before entering an address and paying.
- **What's happening:** The page has opened the payment step for “The Magical Adventure of Linh.” A countdown says the price is reserved for 09:57. The hardcover, pre-selected gift wrap, shipping, total, address field, and card fields are shown.
- **First impression (Minh):** "The total is clear, but £45.97 is more than I expected. I am worried because gift wrap was selected for me without me asking for it."
- **Cognitive walkthrough:** Q1 Yes, I would try removing the gift wrap so I can see the actual hardcover cost with delivery. / Q2 Yes, the checked “Premium gift wrap” checkbox is visible beside its £7.99 price. / Q3 The label clearly describes the extra item, and the checkbox lets me remove it.
  - [DECEPTIVE sev 3] **Gift wrap is selected by default** - evidence: checkbox "Premium gift wrap" (checked), £7.99. Fix: Make every optional extra unchecked by default and label it clearly as an optional add-on. Show how the total changes when it is selected or removed.
  - [VALUE sev 2] **The displayed total does not identify tax** - evidence: “Total £45.97” with no separate VAT or tax line. Fix: Show whether tax is included in the total, or itemise VAT and any other required charges before checkout.
  - [CONTENT sev 2] **The currency changed without explanation** - evidence: Pricing showed “$24.99,” while checkout shows “Hardcover … £24.99”. Fix: Explain why pounds are being used and show the exchange rate, source price, and whether the exchange rate may change.
  - [VALUE sev 2] **The full cost is learned only after ordering** - evidence: The £7.99 gift wrap and £12.99 shipping & handling first appear on the Checkout page.. Fix: Show the starting total for delivery and any optional extras on the pricing page or book page before checkout.
  - [DECEPTIVE sev 1] **A countdown adds pressure to the checkout** - evidence: “Your price is reserved for 09:57”. Fix: State that the price will not change while the customer shops, without using a countdown, or explain exactly when and how the reservation expires.
  - [None sev None] **Removed gift-wrap price still looks active** - evidence: After [6] “Premium gift wrap” is unchecked, “£7.99” remains beside it without being crossed out or labelled as removed.. Fix: When the checkbox is unchecked, cross out the £7.99 price and label it “Not included,” or remove the line completely.
  - [None sev None] **Very short reservation timer creates pressure** - evidence: The message says, “Your price is reserved for 09:42.”. Fix: Remove the timer, or explain the exact condition and give a longer reasonable reservation period without linking it to a payment prompt.
- **Positives:** The hardcover, gift wrap, shipping, and total each have clear prices.; The currency and total are shown together, so the arithmetic is easy to understand.; There is no need to enter payment information to see the current total.

## Generated output assessment
*Artifact:* A nine-page personalized digital story preview with an optional hardcover purchase

> I am disappointed because this does not feel like our family memory. Bà Nội is missing, the special star lantern is not shown properly, the pictures often do not match the words, and the story has serious spelling and ending problems. I would not give this version to Linh or print it as a keepsake.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The story omits the central relationship with Bà Nội and never shows Linh and her grandmother making or floating lanterns together. It also omits the purple áo dài, grey hair in a bun, and the important Hoi An family mem |
| coherence | 1 | The plot jumps from the river festival to heavy rain, an invented uncle, a frightening forest, daylight, and home. The opening is repeated, the following action is confused, and the final sentence is unfinished. |
| age fit | 1 | The measured reading level is grade 6.7 rather than age four, with words such as “ephemeral,” “crepuscular,” “juxtaposing,” and “existential.” The threatening forest and images of shadows growing teeth may also frighten  |
| language | 1 | There are major errors: “Adventrue,” “Lin” instead of “Linh,” unclear pronouns, an unfinished sentence, duplicated “The End,” and unresolved recipient and sender placeholders. |
| text image fit | 1 | Several pictures directly contradict the text, including a sunny picture for a rain scene, a standing child for a child running, and ordinary lanterns for a star-shaped paper lantern. The final lantern-floating scene is  |
| character consistency | 1 | Linh is repeatedly shown with short brown hair and no red ribbon instead of long black hair, round cheeks, and a red ribbon. Bà Nội is absent and replaced by an invented man called Uncle Bartholomew. |
| visual quality | 1 | The images use a simple pop-art style instead of the requested watercolour style. They look generic and do not clearly represent the festival, family relationship, or star-shaped lantern. |
| emotional resonance | 1 | The result feels like a generic and sometimes frightening adventure rather than a warm family keepsake. It does not express Linh's pride in her family, Hoi An, or her memories with Bà Nội. |

- **used correctly:** Linh's name; Linh's age of four; Hoi An; The full-moon lantern festival; The river setting; A red paper lantern shaped like a star
- **missing:** Bà Nội; Linh and Bà Nội making lanterns together; Floating the lanterns on the river; The family-pride message; Bà Nội's purple áo dài; Bà Nội's grey hair in a bun; Linh's long black hair; Linh's red ribbon; Linh's round cheeks; The requested watercolour illustration style; Clear confirmation about premium gift wrap
- **changed:** The special star-shaped lantern became ordinary oval lanterns or a red balloon; The warm grandmother-and-child memory became a generic adventure; The festival setting became a threatening forest in places; The daytime festival atmosphere became an unexplained mixture of day, night, rain, and sunshine; The intended dedication was left as template code; The nine-page preview was described as a twenty-page hardcover without an explanation
- **invented:** Uncle Bartholomew; A sudden rainstorm; A frightening forest; Shadows with teeth; A red balloon; A rocket-shaped object; Unclear language about following the uncle

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic The Magical Adventrue of Linh Linh
- *Picture:* A simple pop-art scene with a short-haired child labelled Linh, a river, four ordinary hanging red lanterns, a bright daytime sun, a rocket-shaped object, and a red oval object. There is no grandmother, no red ribbon, no long black hair, and no clearly star-shaped paper lantern.
- *Reaction:* I can immediately see that “Adventrue” is wrong. The cover does not represent my family memory, and it does not use the watercolour style I wanted.
  - [language, sev 3] The title visibly says “The Magical Adventrue of Linh”; “Adventrue” should be “Adventure”.
  - [fidelity, sev 4] Bà Nội is absent, and the requested red paper lantern shaped like a star is not shown. Linh has short brown hair rather than long black hair with a red ribbon.
  - [visual_quality, sev 3] The picture is labelled “Illustration style: Pop-art comic,” not the requested watercolour style, and the repeated basic shapes do not look like a keepsake family-book cover.
  - [text_image_fit, sev 3] No text on this cover describes a grandmother, but the central family story was supposed to be about Linh and Bà Nội; the picture only shows a child beside a river.
  - [character_consistency, sev 3] The child is shown with short brown hair and no red ribbon instead of Linh's described long black hair with a red ribbon.
  - [emotional_resonance, sev 3] The generic daytime scene feels disconnected from a warm memory of making lanterns with Bà Nội in Hoi An.
- **Change I'd make:** Correct the title and redraw the cover in watercolour as Linh and Bà Nội holding a clear red star-shaped paper lantern beside the river at dusk. Give Linh long black hair, a red ribbon, and round cheeks, and show Bà Nội in a purple áo dài with grey hair in a bun.
- **Suggested rewrite:** Linh and Bà Nội's Star Lantern

#### Title page / Page 2
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A website preview page shows the story title, a mostly blank white panel containing the unresolved dedication, page navigation marked 2/9, a $4.99 regeneration button, and an “Order hardcover” button.
- *Reaction:* This looks unfinished because the names have not been filled in. I cannot tell whether the site lost my information or simply did not ask for these two names.
  - [language, sev 4] The page visibly contains the template code “{{recipient_name}}” and “{{sender_name}}.”
  - [fidelity, sev 3] The recipient should at least be Linh, but the unresolved placeholder does not use the name I supplied.
  - [visual_quality, sev 3] The story title area is a large blank panel with a coding error instead of a finished illustrated dedication page.
- **Change I'd make:** Fill the recipient and sender fields before generating the book. If the sender was not provided, ask me for it rather than showing code. Add a small watercolour picture of the star lantern.
- **Suggested rewrite:** For Linh, with love from Minh and Bà Nội

#### Page 3
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the river in Hoi An at the full-moon lantern festival, there lived a curious child named Linh. Linh was 4 years old and loved nothing more than a red paper lantern shaped like a star.
- *Picture:* The same simple child from the cover stands on the bank of blue water beneath four ordinary hanging red lanterns and a large daytime sun. There is no Bà Nội, no crafting activity, and no star-shaped lantern.
- *Reaction:* The opening names Linh, Hoi An, the age, and the special lantern, but the picture and the sentence do not make the family memory clear. Also, children and families do not normally live “in the river.”
  - [language, sev 3] The sentence says “in the river in Hoi An ... there lived a curious child,” which is grammatically and physically misleading.
  - [fidelity, sev 4] Bà Nội and the action of making the lantern together are missing, even though they are central to my memory.
  - [text_image_fit, sev 3] The text describes a red paper lantern shaped like a star, but the picture shows only smooth red oval lanterns and a separate red oval object.
  - [character_consistency, sev 3] Linh has short brown hair with no red ribbon, not the requested long black hair with a red ribbon.
  - [visual_quality, sev 2] The image is a flat generic pop-art scene rather than the chosen watercolour style.
- **Change I'd make:** Put Linh and Bà Nội beside the river at dusk, making the star-shaped lantern together. Use short sentences and describe the riverbank rather than saying that they live in the river.
- **Suggested rewrite:** It was the full-moon lantern festival in Hoi An. Linh stood beside the river with her grandmother, Bà Nội. Together, they made a red paper lantern shaped like a star.

#### Page 4
![I4](artifacts/capture_05/img_00.jpg)
> One evening Linh gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Linh stands front-facing beside the river while the sky changes to purple and red with a few stars. The ordinary hanging red lanterns remain, but she is not clearly looking upward and Bà Nội is absent.
- *Reaction:* I need my phone to understand this sentence, so it is not suitable for four-year-old Linh or for an adult reader with intermediate English. The picture also misses what Linh is doing.
  - [age_fit, sev 4] The text uses “ephemeral,” “crepuscular,” “luminescence,” “engendered,” “melancholy,” “juxtaposing,” “ineffable,” and “existential trepidation.” The measured grade level is 6.7, not a reading age of four.
  - [language, sev 4] The long sentence is difficult to understand and is not written in simple story language for the requested audience.
  - [fidelity, sev 4] The requested shared lantern-making memory is replaced by a vague mood passage, and Bà Nội is absent.
  - [text_image_fit, sev 2] The text says Linh “gazed upward,” but her eyes face forward in the picture.
  - [character_consistency, sev 2] The same short-haired child is used, rather than Linh with long black hair and a red ribbon.
- **Change I'd make:** Replace the difficult sentence with simple language about Linh and Bà Nội choosing colours and drawing a star for the lantern. Show Linh looking up at the evening sky and include both characters.
- **Suggested rewrite:** Linh looked at the purple evening sky. “Let’s make our star shine tonight,” Bà Nội said. Linh smiled and picked up the red paper.

#### Page 5
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Lin pulled up her hood and ran for shelter, holding a red paper lantern shaped like a star tight.
- *Picture:* The scene is bright and sunny, with no rain, puddles, hood, running child, or shelter. Linh stands still beside the river, and the nearby objects still do not include a star-shaped lantern.
- *Reaction:* The words and picture tell opposite stories. I would not let Linh read this page with this picture because the rain is completely missing.
  - [text_image_fit, sev 4] The text says rain poured, drops hit puddles, Linh pulled up her hood, and she ran for shelter, while the image has a clear sun and a stationary child.
  - [language, sev 3] The name is printed as “Lin” in “Lin pulled up her hood.”
  - [fidelity, sev 3] Bà Nội and the grandmother-and-child lantern journey are missing.
  - [character_consistency, sev 3] Linh again has short brown hair and no red ribbon or clearly visible round-cheeked appearance matching the requested description.
- **Change I'd make:** Correct “Lin” to “Linh” and redraw the page with rain, puddles, Linh wearing a rain hood, and Bà Nội helping her protect the star-shaped lantern. Alternatively, remove the rain and keep the story at the festival.
- **Suggested rewrite:** Rain began to fall. Linh held her star lantern close to her chest. Bà Nội opened her umbrella, and they walked together under the rain.

#### Page 6
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Linh, follow me!" he called, and he followed him along the winding path.
- *Picture:* A blue-clothed adult man labelled “Uncle Bartholomew” stands beside Linh near the river. Bà Nội is not shown, no winding path appears, and the man's object is a small yellow square rather than a clear lantern.
- *Reaction:* I did not ask for Uncle Bartholomew. The sentence also says “he followed him,” which is confusing because Linh should be following the uncle.
  - [fidelity, sev 4] The story invents “Uncle Bartholomew” and removes the requested grandmother, Bà Nội, even though she was the only other person I requested.
  - [language, sev 3] The sentence says “he called, and he followed him,” even though the uncle is the person already leading the way.
  - [coherence, sev 3] There is no clear reason for the uncle to appear, and the person following him changes without explanation.
  - [text_image_fit, sev 3] The text mentions Linh following the uncle along a winding path, but the picture shows both characters standing still beside the river with no path.
  - [character_consistency, sev 4] The adult is not Bà Nội: the picture shows a man in blue rather than an older woman in a purple áo dài with grey hair in a bun.
- **Change I'd make:** Delete Uncle Bartholomew and make Bà Nội the adult in this scene. Show Linh and Bà Nội walking together while carrying the finished lantern.
- **Suggested rewrite:** “Come with me, Linh,” Bà Nội said. Linh took her grandmother’s hand. Together, they walked towards the river with their red star lantern.

#### Page 7
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Linh again. Linh clutched a shiny red balloon and trembled in the dark.
- *Picture:* Linh stands at night near three simple trees, a crescent moon, and stars, holding or standing beside a red oval balloon. There are no visible shadows with teeth, no whispering danger, and no Bà Nội.
- *Reaction:* This dark threat is frightening and it does not belong in the calm family festival memory I wanted. It also changes the special paper lantern into a red balloon.
  - [fidelity, sev 4] The story leaves the Hoi An river setting for threatening woods and replaces the red star-shaped paper lantern with a shiny red balloon.
  - [age_fit, sev 4] The threats that shadows “grew teeth” and that no one would “ever find Linh again” may frighten a four-year-old.
  - [coherence, sev 4] The page jumps suddenly from walking with an uncle into a dangerous forest, without explaining why Linh went there.
  - [text_image_fit, sev 3] The text describes shadows growing teeth and whispering, but the picture shows ordinary round tree tops with no frightening shapes.
  - [character_consistency, sev 3] Linh still has short brown hair and no red ribbon, and the previous adult character has disappeared.
- **Change I'd make:** Remove the frightening forest sequence. Return to the river and show Linh and Bà Nội safely placing the star lantern on the water.
- **Suggested rewrite:** Linh and Bà Nội knelt beside the river. They placed their red star lantern on the water. The warm light shone around Linh’s face.

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the river in Hoi An at the full-moon lantern festival, there lived a curious child named Linh. At last the sun came out, and Linh skipped all the way home, happier than ever.
- *Picture:* Linh stands still beside the river in daylight beneath a large sun and four ordinary hanging red lanterns. She is not shown skipping or walking home, and no grandmother or lanterns floating on the water are visible.
- *Reaction:* The story repeats the opening instead of continuing the family memory, then jumps from night to sun and home. I cannot see the important moment when Linh floats her lantern on the river.
  - [coherence, sev 4] The sentence beginning “Once upon a time” is repeated from the opening, so the plot resets and does not provide a proper conclusion to the lantern journey.
  - [fidelity, sev 4] The requested action of Linh and Bà Nội floating the lanterns on the water never occurs. Bà Nội is absent.
  - [text_image_fit, sev 3] The text says Linh “skipped all the way home,” while the picture shows her standing still beside the river in daylight.
  - [age_fit, sev 2] “At last the sun came out, and Linh skipped all the way home, happier than ever” is understandable, but the repeated opening makes it confusing rather than meaningful.
  - [character_consistency, sev 3] Linh retains the same generic short-haired design but still does not match her requested long black hair and red ribbon.
- **Change I'd make:** Remove the repeated opening and make this the emotional festival climax: Linh and Bà Nội float the lanterns, Linh sees the star reflected in the river, and they feel proud of their family.
- **Suggested rewrite:** Linh and Bà Nội gently placed the star lantern on the river. It floated with the other lanterns. “This light is for our family,” Bà Nội said. Linh smiled with pride.

#### Page 9 / End page
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Linh looked up at the sky, she would always remember The End
- *Picture:* An orange evening scene shows Linh beside the river under four ordinary hanging red lanterns, with “The End” printed near the top. The family, floating star lantern, festival activity, and finished memory are absent.
- *Reaction:* The last thought stops in the middle of a sentence, and “The End” is printed twice. This is not ready to give to Linh or to print.
  - [language, sev 4] The sentence “And from that day on, whenever Linh looked up at the sky, she would always remember” has no finishing thought, and “The End” appears twice.
  - [coherence, sev 4] The page has no completed emotional conclusion because the final memory is unfinished.
  - [fidelity, sev 4] The ending does not name Bà Nội or explain what Linh would remember about their family, Hoi An, or the festival.
  - [text_image_fit, sev 3] The image does not show Linh looking at the sky; she faces forward, and the promised memory is not pictured.
  - [emotional_resonance, sev 4] An unfinished sentence and duplicated ending make the family keepsake feel broken rather than personal.
- **Change I'd make:** Complete the final memory in one short sentence, show Linh and Bà Nội together, and print “The End” only once. The final picture should be in the chosen watercolour style.
- **Suggested rewrite:** From then on, whenever Linh saw a lantern glowing, she remembered the day she made a star with Bà Nội in Hoi An.  The End

#### Pricing page
![I10](artifacts/capture_13/view_00.jpg)
![I11](artifacts/capture_13/view_01.jpg)
> Simple pricing Digital preview Free Create and read your illustrated story online. Hardcover book $24.99 20 glossy pages, printed and bound to last. New version $4.99 Want a different story? Generate a brand-new version of your book. Start your book
- *Picture:* Two identical screenshots show three pricing cards. The hardcover price is $24.99 for 20 glossy pages, a different story version costs $4.99, and the digital preview is free.
- *Reaction:* The main prices are visible, but I cannot understand why my nine-page online preview will become a 20-page hardcover. I also cannot tell whether the $24.99 includes the premium gift wrap I selected.
  - [language, sev 3] The page does not explain the page-count difference between the “Preview · 9 pages” and the “20 glossy pages” hardcover.
  - [fidelity, sev 3] The requested “Premium gift wrap” is not named on the pricing page, and there is no statement that it is included, costs extra, or was ignored.
  - [emotional_resonance, sev 3] Because the final total and included options are unclear, the page does not give me enough confidence to purchase this intended keepsake.
- **Change I'd make:** Add a plain-language explanation of why the preview has nine pages and the hardcover has 20, state the exact final cost, and show whether premium gift wrap is included or costs extra before the checkout button.
- **Suggested rewrite:** Digital preview: Free, 9 pages. Hardcover: $24.99, 20 pages, including premium gift wrap. Shipping and any other charges will be shown before you pay.

#### Dashboard
![I12](artifacts/capture_14/view_00.jpg)
![I13](artifacts/capture_14/view_01.jpg)
> ⚠ Error 0x80070057: profile sync incomplete. Welcome back, Demo Preview ready Open + Create a new book
- *Picture:* The visible screenshot is a StoryHearth account page with a warning banner, the title “The Magical Adventrue of Linh,” a Preview ready card with an Open button, and a Create a new book button. I13 is listed in the capture but is not provided for inspection.
- *Reaction:* The technical error makes me worry that my profile or story information is incomplete. It also greets “Demo” instead of Minh, and the misspelled title is still there.
  - [language, sev 3] The banner says “Error 0x80070057: profile sync incomplete,” which does not explain what failed or what action I should take.
  - [fidelity, sev 3] The dashboard says “Welcome back, Demo” even though the supplied email is “demo.family@storyhearth.test”; it is unclear whether my real profile name was saved.
  - [language, sev 3] The dashboard repeats the title “The Magical Adventrue of Linh.”
  - [emotional_resonance, sev 3] Showing an unexplained sync error next to “Preview ready” makes me doubt whether the purchased or generated book is complete.
- **Change I'd make:** Replace the error code with a message such as “We could not save your profile. Your book is safe. Please check your details and try again.” Show which information is missing and correct the title everywhere.
- **Suggested rewrite:** Your profile has not finished syncing. Your book is safe. Please check your name and email, then select Try again. If the problem continues, contact support.

**Top changes to the output:** 1. Rebuild the entire story around Linh and Bà Nội making the red star-shaped lantern and floating it on the river at the Hoi An festival. | 2. Remove Uncle Bartholomew, the frightening forest, the red balloon, and all unrelated adventure events. | 3. Replace the difficult vocabulary and long sentences with simple English suitable for a four-year-old. | 4. Correct all text errors, including “Adventure,” “Linh,” the unresolved dedication placeholders, the repeated opening, and the unfinished ending. | 5. Redraw every page in watercolour with consistent Linh and Bà Nội character designs and pictures that accurately match the text. | 6. Explain the nine-page versus twenty-page difference and confirm the exact price and whether premium gift wrap is included before payment.

## Recommendations (participant's priorities)
- **[high] Rebuild the story around Linh and Bà Nội making the red star-shaped lantern and floating it on the river at the Hoi An festival.** (Generated storybook preview) - This is the most important memory, so the book must keep the family relationship, place, culture, and special object.
- **[high] Remove unrelated and frightening things such as Uncle Bartholomew, the forest, heavy rain, and the red balloon.** (Generated storybook preview) - I want a warm family story for Linh, not a frightening or confusing adventure.
- **[high] Use simple English, short sentences, and vocabulary suitable for a four-year-old.** (Reading level and illustration style) - Words such as “ephemeral” are too difficult, and the story should be read aloud to Linh.
- **[high] Correct spelling and unfinished text, including “Adventure,” “Linh,” the repeated opening, and the incomplete final sentence.** (Generated storybook preview) - These errors make the book look unfinished and prevent me from giving it to my daughter.
- **[high] Make every picture match the words and use the selected soft watercolour style.** (Generated storybook preview) - The comic pictures did not match the story or my choice, so they did not feel like our memory.
- **[high] Keep Linh and Bà Nội consistent in every picture, with Linh's long black hair and red ribbon and Bà Nội's grey bun and purple áo dài.** (Generated storybook preview) - The characters are the heart of the story and must not be changed.
- **[high] Explain every error and give clear steps for fixing it, especially “profile sync incomplete.”** (My books dashboard) - I did not know what the error meant or what I should do next.
- **[high] Explain the loading process and show the current step, with a safe way to stop or leave.** (Book creation loading page) - The loading circle made me think the book had failed or that I needed to press something.
- **[high] Explain Lexile in plain English and show a clear reading level for children aged four.** (Reading level and illustration style) - I did not know what Lexile means, and the generated story was much too difficult for Linh.
- **[high] Show the complete price, currency, tax, postage, page count, and optional gift wrap before the user clicks “Order hardcover.”** (Pricing and Checkout) - I was surprised by the £45.97 total, the currency change, and gift wrap being selected by default.
- **[medium] Explain the difference between the nine-page online story and the twenty-page hardcover, and let me order the current book from the pricing page.** (Simple pricing) - I need to know exactly what I would receive and what it would cost before leaving the book page.
- **[medium] Add clear fields for every important character, including appearance and relationship, and support Vietnamese names and cultural details.** (Create your book – character details) - I could not fully describe Bà Nội or confirm that “Bà Nội” would be kept correctly.
- **[medium] Explain photo privacy and how long uploaded photos are kept, and add a visible label for the upload area.** (Add a photo) - Family photos are private, and I need to know how they are used before uploading them.
- **[low] Replace difficult marketing language and provide a visible way to recover a forgotten password.** (Home page and Log in) - The difficult words slowed me down, and I could not see how to recover my account if I forgot the password.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This website is for making personal storybooks with family members and memories. I think it is for parents who want a special story about their family and culture.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the finished book. It changed Linh, left out Bà Nội, used the wrong pictures and style, and had spelling and ending problems. The unclear loading screen and profile sync error also made me worried.
- **What was the best moment?** The best moment was when I could see and change the total price after removing the premium gift wrap. I felt more in control when the site clearly showed that the price changed.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have stopped before payment, when I saw that the book was not about our family memory. I would not want to pay for a keepsake that was not right.
- **What did you expect to find or be able to do that wasn't there?** I expected the book to show Linh and Bà Nội making and floating the red star-shaped lantern at the Hoi An festival. I also expected fields for Bà Nội's appearance and relationship, and a clear reading level for a four-year-old.
- **Did you trust this website with your information (and your family's)? Why or why not?** I would be careful about sharing family photos and personal information because the privacy and retention details were not explained on the upload page. I also did not trust the final book because it changed my family details.
- **If the site produced something for you, how do you feel about it overall?** I am very disappointed. This does not feel like our family memory, and I would not give it to Linh or print it as a keepsake.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | I understand that this website makes storybooks using my family memories. The main explanation is quite clear, but the sentence with “multimodal generative narrative engine” is difficult for me. I need to log in first wi | click |
| 2 | Log in – StoryHearth | reassured (1) | The form looks simple and I understand what to do. I can enter my account email and password. I do notice the footer links are very faint, but I do not need them now. | type; type; click |
| 3 | My books – StoryHearth | confused (-1) | The login worked because I can see “Welcome back, Demo” and the “Log out” link. I want to create our story, so I will use “+ Create a new book.” The error message is worrying because I do not understand what “profile syn | click |
| 4 | Create your book – StoryHearth | curious (1) | This form is simple and I can understand it. I will enter Linh exactly as her name is written. I hope the website will keep the name “Bà Nội” and our Vietnamese culture correct. | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | curious (1) | The labels are clear and I understand what to enter. I will give the exact place, the red star-shaped paper lantern, and the memory of Linh making lanterns with Bà Nội. I hope the website will not change the name Bà Nội  | type; type; type; click |
| 6 | Create your book – StoryHearth | curious (1) | The layout is clear, but I do not know what “Lexile” means. Because Linh is four, I think the youngest range, “Lexile BR–200L,” is safer. The watercolour pictures look gentle and nice, so I will keep that and continue. | click; click |
| 7 | Create your book – StoryHearth | reassured (1) | This step is simple. I do not have a photo file ready here, and the photo is optional, so I will continue without one. I hope the book will still show Linh’s red ribbon and our Vietnamese family correctly. | click |
| 8 | Create your book – StoryHearth | hesitant (-1) | I think the website is making the book, but the loading circle does not tell me what is happening. I do not know if I should wait, if the story failed, or if I need to do something else. | wait_for_change |
| 9 | Your storybook – StoryHearth | frustrated (-2) | The book was made, so that is clear, but I am disappointed by “Adventrue.” It should say “Adventure.” The picture also looks like a simple comic, not the soft watercolour style I chose. I need to read all nine pages and  | flip_through |
| 10 | Your storybook – StoryHearth | frustrated (-1) | I have now read all nine pages. The last sentence feels unfinished: “And from that day on, whenever Linh looked up at the sky, she would always remember”. I also do not see our red star-shaped lantern or Bà Nội clearly i | scroll |
| 11 | Your storybook – StoryHearth | frustrated (-1) | I have read all nine pages, and the last sentence still feels unfinished. The picture also does not show the red star-shaped lantern clearly, so I am not happy with this book. I do not want to spend $4.99 to change it. I | click |
| 12 | Pricing – StoryHearth | reassured (1) | Now I can see the hardcover price: $24.99. This is clear, but I am worried because my online story has only 9 pages while the hardcover says 20 pages. I also need to know if £ conversion, postage, and tax are extra befor | click |
| 13 | My books – StoryHearth | frustrated (-1) | Yes, the book is saved and I can open it. I will go back to the book and use “Order hardcover” to check the final cost, but I will not enter payment details or pay. | click |
| 14 | Your storybook – StoryHearth | frustrated (-1) | The book opened correctly, so I can find the ordering button. I still do not like the spelling or pictures, but I will first check the full hardcover cost. I will not pay or enter payment details. | scroll |
| 15 | Your storybook – StoryHearth | frustrated (-1) | Now I can see “Order hardcover.” I will click it to check the real final cost. I will not enter any payment details or pay. | click |
| 16 | Checkout – StoryHearth | suspicious (-1) | The real checkout cost is £45.97, but I did not ask for “Premium gift wrap,” and it was already selected. I will remove it to understand the price without an extra item, but I will not enter my address or card details an | click |
| 17 | Checkout – StoryHearth | reassured (1) | Good, the site clearly showed that removing gift wrap changed the total. I now know the real cost without gift wrap is £37.98. I will not enter my address or card details, and I will not click “Pay now.” | done |
