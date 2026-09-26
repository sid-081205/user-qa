# UserQA report: Test User on http://127.0.0.1:8765/

*Persona:* **Test User** (35) - Baseline condition - a generic adult web user with no persona conditioning (ablation).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 11 steps | *Pages reviewed:* 9 | *Issues:* 26 | *LLM calls:* 13 | *Wall time:* 254.7 s

## What the agent understood the website to be
- **what it is:** A website that creates personalised, illustrated family storybooks from supplied characters and memories.
- **who it is for:** Families wanting to preserve a child and another family member in a story, including as a printed keepsake.
- **value proposition:** Turn a family memory into a fully illustrated storybook that can be previewed digitally and potentially printed as a UK-shipped hardcover.
- **pricing model:** The page says the digital preview is free and printed hardcovers are available, but it gives no actual price.
- **fit for me:** It sounds relevant because I want a story about Sam and Grandpa Joe at the beach, and I can read the preview before considering a printed copy.
- **main tasks:** Log in, Add the child and another person as characters, Describe a place, treasured object, and memory, Generate and read the illustrated storybook, Check the price of a printed hardcover

## Scores
- SUS: **55.0** (grade D; 68 = industry average) - inconsistent responding flagged
- UEQ-S: pragmatic -0.75, hedonic 0.25 (range -3..+3)
- Likelihood to recommend (0-10): 0
- Output keepsake-worthiness (1-5): 1
- Verdict: *"Warm idea and easy forms, but the inaccurate, frightening, unfinished book would make me walk away without paying."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Unhelpful technical error message | “Error 0x80070057: profile sync incomplete.” | Replace the raw code with a plain-language message such as “We couldn't finish loading your profile. Your books are safe. Try again, or contact support if this continues,” and include a clear Retry co |
| 3 | H4 | Generated storybook preview | Selected illustration style was not applied | The page says "Illustration style: Pop-art comic," but the previously selected style was "Watercolour — soft and dreamy." | Use the selected style consistently and show the selected setting beside the preview, or explain if the style cannot be applied. |
| 3 | CONTENT | Generated storybook preview | Cover does not match the submitted family memory | The cover shows a generic figure, sun, star, and water, while the story details were "the beach," a "yellow bucket," and building sandcastles with Grandpa Joe. | Generate the cover from the supplied memory and show the main people, place, and object clearly, with an option to regenerate if details are wrong. |
| 3 | CONTENT | Generated storybook preview | Final page ends with an incomplete sentence | “And from that day on, whenever Sam looked up at the sky, she would always remember” | Check the generated text before presenting the book and complete or remove any incomplete final sentence. |
| 3 | DECEPTIVE | Hardcover checkout | Optional gift wrap is selected by default | [6] checkbox "Premium gift wrap" (checked), adding "£7.99" | Make all optional extras unchecked by default and show the delivered hardcover total before asking the customer to opt in. |
| 2 | ACC | Log in form, My books dashboard, Story details form, Optional photo upload (x4) | Footer links and copyright have very low contrast | “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” appear extremely faint in the footer. | Increase the footer text and link contrast to meet accessible colour-contrast guidelines. |
| 2 | CONTENT | Generated storybook preview, Hardcover checkout (x2) | Title contains a spelling error | "The Magical Adventrue of Sam" | Correct the title to "The Magical Adventure of Sam" before showing the generated book. |
| 2 | CONTENT | StoryHearth homepage | The main description uses confusing technical jargon | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace it with plain language such as: “Turn a treasured family memory into a beautifully illustrated story starring your child and someone you love.” |
| 2 | ACC | StoryHearth homepage | Main illustration has no accessible description | [image (no description) 430x440] | Add suitable alt text, or mark the image decorative with empty alt text if the surrounding text already conveys its meaning. |
| 2 | ACC | Log in form | Input fields have no visible labels | [5] and [6] are described as “textbox (no label)” and rely on the placeholders “Email” and “Password.” | Add persistent visible labels for the email and password fields, associated with their controls. |
| 2 | TRUST | My books dashboard | Error warning may undermine confidence in account data | The warning appears immediately above “Welcome back, Demo,” with no reassurance about what remains usable. | State explicitly whether account and profile data are safe, explain any impact on book creation, and provide a support route if the sync still fails. |
| 2 | H2 | Create your book form | Relationship defaults to Grandparent without explanation | [11] combobox "Relationship" shows "Grandparent" as the selected value before I choose anyone. | Start the relationship dropdown at “Select…” and require a choice, or clearly mark the preselected value as an intentional default. |
| 2 | H2 | Look and feel settings | Reading-level choices use unexplained jargon | The heading says “Reading level” and the options are labelled “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+.” | Show familiar age or difficulty labels first, such as “Ages 4–7 — early reader,” with the Lexile range as secondary text and optionally a one-sentence explanation. |
| 2 | CONTENT | Generated storybook preview | Character details may not have been preserved | The earlier profile said Sam has brown hair, and Grandpa Joe has grey hair, but the visible cover only shows Sam and gives no clear evidence of Grandpa Joe or h | Carry the character names, relationships, appearances, and pronouns into the story and make sure Grandpa Joe appears in relevant pages. |
| 2 | CONTENT | Generated storybook preview | The generated artwork does not clearly match the requested beach memory | The final picture shows Sam against a simple sky-and-water background, with no visible yellow bucket, sandcastles, or Grandpa Joe. | Include the supplied place, special object, characters, and memory details in the generated illustrations, and provide a clear way to regenerate or edit an individual page. |

## Page-by-page
### StoryHearth homepage  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the personalised family storybook service and lead visitors toward creating a story or viewing prices.
- **What's happening:** The landing page shows the service proposition, a “Proceed” button, a pricing link, a free-preview and UK-shipping statement, three creation steps, family testimonials, FAQ controls, and policy/contact links.
- **First impression (Test):** "It looks warm and appealing, with a friendly illustration, but the main sentence is unnecessarily technical and makes the service sound more like AI jargon than something made for families."
- **Cognitive walkthrough:** Q1 Yes, because “1. Tell us who,” “2. Share a memory,” and “3. We write & illustrate” suggest I can create the story I want. / Q2 Yes, the orange “Proceed →” button is prominent, and there is also a clearly visible “Log in” button in the header. / Q3 Mostly. “Proceed” could mean starting or continuing, while “Log in” clearly matches my immediate goal of accessing my account.
  - [CONTENT sev 2] **The main description uses confusing technical jargon** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace it with plain language such as: “Turn a treasured family memory into a beautifully illustrated story starring your child and someone you love.”
  - [ACC sev 2] **Main illustration has no accessible description** - evidence: [image (no description) 430x440]. Fix: Add suitable alt text, or mark the image decorative with empty alt text if the surrounding text already conveys its meaning.
  - [TRUST sev 1] **Testimonials provide little verifiable detail** - evidence: “My daughter asks for ‘her’ book every single night.” — Hannah, Leeds. Fix: Add a clearly labelled review source, fuller review criteria, or links to verified customer reviews.
- **Positives:** The warm colours and family-themed illustration create an inviting tone.; The three-step explanation makes the overall process easy to understand.; The site clearly says the digital preview is free.; “Log in” is prominent in the header.

### Log in form  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Allow an existing StoryHearth user to access their account and create a personalised family storybook.
- **What's happening:** The page presents email and password entry fields, a “Log in” button, and a “Create an account” link.
- **First impression (Test):** "This looks straightforward and trustworthy. The warm colours and simple layout make the form easy to understand."
- **Cognitive walkthrough:** Q1 Yes, I would try to log in now because the form is prominently displayed. / Q2 Yes, I immediately notice the email field, password field, and “Log in” button. / Q3 Yes, “Log in” clearly matches what I want to do. The field placeholders also make sense, although permanent labels would be better.
  - [ACC sev 2] **Input fields have no visible labels** - evidence: [5] and [6] are described as “textbox (no label)” and rely on the placeholders “Email” and “Password.”. Fix: Add persistent visible labels for the email and password fields, associated with their controls.
  - [ACC sev 2] **Footer links and copyright have very low contrast** - evidence: “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” appear extremely faint in the footer.. Fix: Increase the footer text and link contrast to meet accessible colour-contrast guidelines.
- **Positives:** The “Welcome back” heading makes the purpose of the page clear.; The orange “Log in” button is prominent and easy to find.; The page provides a clear alternative for new users with “Create an account.”; The layout is uncluttered and the form is easy to understand.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the signed-in user's saved books and provide a way to create another one.
- **What's happening:** The page confirms that Demo is logged in, reports that there are no books yet, and displays a profile-sync warning. The main available task is creating a new book.
- **First impression (Test):** "The page is simple and the orange “+ Create a new book” button stands out, but the unexplained technical error immediately makes me wonder whether something has gone wrong with my account."
- **Cognitive walkthrough:** Q1 Yes, because I need to create a storybook and this is the only obvious creation control. / Q2 Yes, the orange “+ Create a new book” button is prominent directly beneath the empty-books message. / Q3 Yes, “Create a new book” clearly matches what I want to do.
  - [H9 sev 3] **Unhelpful technical error message** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the raw code with a plain-language message such as “We couldn't finish loading your profile. Your books are safe. Try again, or contact support if this continues,” and include a clear Retry control if retrying is useful.
  - [TRUST sev 2] **Error warning may undermine confidence in account data** - evidence: The warning appears immediately above “Welcome back, Demo,” with no reassurance about what remains usable.. Fix: State explicitly whether account and profile data are safe, explain any impact on book creation, and provide a support route if the sync still fails.
  - [ACC sev 2] **Footer text has weak visual contrast** - evidence: The “Privacy,” “Terms,” “Contact,” and copyright text is extremely pale grey against the white footer.. Fix: Use a darker text colour that meets WCAG contrast requirements and ensure the links remain visibly distinguishable.
- **Positives:** The dashboard clearly states “You have no books yet,” so the empty state is easy to understand.; The “+ Create a new book” button is prominent and uses a label that directly matches my task.; The signed-in state is confirmed by the welcome heading and visible “Log out” link.

### Create your book form  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect basic details about the child who will star in the story and the other person who will appear.
- **What's happening:** The form is empty and ready for input. It includes fields for the child's first name, age, pronouns, appearance, another character, and that character's relationship, followed by a Next button.
- **First impression (Test):** "This looks clean and easy to scan. I understand what the form is asking, and the orange Next button stands out."
- **Cognitive walkthrough:** Q1 Yes, I would enter the character details now because they are needed to make the story personal. / Q2 Yes, I noticed the relevant textboxes and dropdowns, plus the Next button. / Q3 Yes. “Who’s the star of the story?” and “Who else is in the story?” match what I want to do.
  - [H2 sev 2] **Relationship defaults to Grandparent without explanation** - evidence: [11] combobox "Relationship" shows "Grandparent" as the selected value before I choose anyone.. Fix: Start the relationship dropdown at “Select…” and require a choice, or clearly mark the preselected value as an intentional default.
  - [H2 sev 1] **The form does not yet show where to enter the family memory** - evidence: The visible form ends after “Who else is in the story?” and the “Next” button; no memory or occasion field is visible.. Fix: Add a brief prompt or progress indicator explaining that the next step will ask for the memory or occasion.
- **Positives:** The page has a clear question-style heading.; The fields are grouped logically for the child and the other character.; The visible labels make the form understandable even though some placeholders are faint.; The Next button is prominent and easy to find.

### Story details form  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, meaningful object, and family memory needed to create the personalised story.
- **What's happening:** The story-creation form has moved to the “Your story” stage. Empty controls are provided for the location, a special object, and the memory or idea behind the story, followed by Back and Next.
- **First impression (Test):** "The layout is calm and straightforward, and the questions help me recall the right details without making me think too much."
- **Cognitive walkthrough:** Q1 Yes, I would fill in these three fields now. / Q2 Yes, the fields are prominent under “Your story,” and the orange “Next” button is easy to find. / Q3 Yes. “Where does the story happen?”, “A special object,” and “Tell us the memory or idea behind your story” clearly match what I want to add.
  - [H1 sev 1] **Saved character details are not confirmed** - evidence: The screen only shows “Your story” and three empty fields; there is no summary confirming that Sam and Grandpa Joe were retained from the previous screen.. Fix: Show a compact summary above the form, such as “Hero: Sam, age 5, she/her, brown hair; Also in the story: Grandpa Joe,” with an Edit link.
  - [ACC sev 1] **Footer text has very low contrast** - evidence: The “Privacy,” “Terms,” and “Contact” footer text is extremely faint against the white background.. Fix: Use a darker footer text colour that meets WCAG contrast requirements while retaining the subdued appearance.
- **Positives:** The three prompts are written in plain, family-friendly language.; The form is uncluttered and the primary Next action is visually prominent.; Back is available, so I do not feel trapped in this step.

### Look and feel settings  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose the reading difficulty and illustration style for the personalised book.
- **What's happening:** The page offers four Lexile reading ranges and three illustration styles. Lexile 200L–500L and Watercolour are currently selected, and I can continue or go back.
- **First impression (Test):** "This looks tidy and manageable, but “Lexile” is jargon that makes the reading-level choices less immediately understandable."
- **Cognitive walkthrough:** Q1 Yes, I would try to choose options that suit Sam’s reading age and the family memory. / Q2 Yes, the reading level and illustration style radio groups are clearly visible, as is the Next button. / Q3 Partly. The illustration labels clearly match my goal, but the Lexile ranges do not plainly explain the intended reading age or difficulty.
  - [H2 sev 2] **Reading-level choices use unexplained jargon** - evidence: The heading says “Reading level” and the options are labelled “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+.”. Fix: Show familiar age or difficulty labels first, such as “Ages 4–7 — early reader,” with the Lexile range as secondary text and optionally a one-sentence explanation.
  - [H1 sev 1] **The preselected reading level is not explained** - evidence: “Lexile 200L–500L” is checked when the page appears.. Fix: Add text such as “Recommended from Sam’s age: 5” or “Default: suitable for early readers.”
- **Positives:** The selected states are clearly visible.; The illustration choices have plain-language descriptions.; Back and Next controls are easy to find.

### Optional photo upload  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Offer an optional child photo before creating the personalised book.
- **What's happening:** The user can upload an image, go back to the previous step, or create the book without a photo. The prominent “Create my book” button is available.
- **First impression (Test):** "This looks neat and the photo is clearly optional. I’m happy to continue without one, although the footer is almost too faint to read."
- **Cognitive walkthrough:** Q1 Yes, I would continue by creating the book without uploading a photo. / Q2 Yes, “Create my book” is large, teal, and on the right, so it is easy to notice. / Q3 Yes. “Create my book” clearly says that this will create the personalised book rather than merely save the draft.
  - [ACC sev 1] **Footer text has very low contrast** - evidence: The footer links and copyright text, including “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.”, are extremely faint against the background.. Fix: Increase the footer text colour contrast to meet WCAG AA standards.
  - [ACC sev 1] **File upload control lacks a persistent associated label** - evidence: [30] is a “file-upload (no label)” and only shows the native “Choose file / No file chosen” control.. Fix: Add a persistent visible label such as “Child photo” and programmatically associate it with the file input.
- **Positives:** “Add a photo (optional)” makes it clear that skipping the upload is allowed.; The explanation gives a useful reason to upload a photo.; The main “Create my book” button is prominent and clearly labelled.; A visible Back button gives me control before committing.

### Generated storybook preview  (step 8)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Preview the generated family storybook and read through all of its pages.
- **What's happening:** A 9-page book titled "The Magical Adventrue of Sam" is displayed. The cover includes Sam, a sun, a star, and water, but the surrounding information says "Illustration style: Pop-art comic." Controls are available to move through the pages, with the previous control disabled on page 1.
- **First impression (Test):** "I can tell a book was created, but the title typo and the mismatch with my beach memory make me uncertain that the site used the information I entered. The cover does not look like a personalised family memory book."
- **Cognitive walkthrough:** Q1 Yes, I would try to read through the preview because I need to check whether it contains the beach, sandcastles, Grandpa Joe, and the yellow bucket. / Q2 Yes, I noticed the right arrow and the "1 / 9" page indicator. / Q3 The right arrow is understandable, but "Preview" is clear enough. I would prefer a more explicit "Next page" label.
  - [H4 sev 3] **Selected illustration style was not applied** - evidence: The page says "Illustration style: Pop-art comic," but the previously selected style was "Watercolour — soft and dreamy.". Fix: Use the selected style consistently and show the selected setting beside the preview, or explain if the style cannot be applied.
  - [CONTENT sev 3] **Cover does not match the submitted family memory** - evidence: The cover shows a generic figure, sun, star, and water, while the story details were "the beach," a "yellow bucket," and building sandcastles with Grandpa Joe.. Fix: Generate the cover from the supplied memory and show the main people, place, and object clearly, with an option to regenerate if details are wrong.
  - [CONTENT sev 3] **Final page ends with an incomplete sentence** - evidence: “And from that day on, whenever Sam looked up at the sky, she would always remember”. Fix: Check the generated text before presenting the book and complete or remove any incomplete final sentence.
  - [CONTENT sev 2] **Title contains a spelling error** - evidence: "The Magical Adventrue of Sam". Fix: Correct the title to "The Magical Adventure of Sam" before showing the generated book.
  - [CONTENT sev 2] **Character details may not have been preserved** - evidence: The earlier profile said Sam has brown hair, and Grandpa Joe has grey hair, but the visible cover only shows Sam and gives no clear evidence of Grandpa Joe or his appearance.. Fix: Carry the character names, relationships, appearances, and pronouns into the story and make sure Grandpa Joe appears in relevant pages.
  - [CONTENT sev 2] **The generated artwork does not clearly match the requested beach memory** - evidence: The final picture shows Sam against a simple sky-and-water background, with no visible yellow bucket, sandcastles, or Grandpa Joe.. Fix: Include the supplied place, special object, characters, and memory details in the generated illustrations, and provide a clear way to regenerate or edit an individual page.
- **Positives:** The page clearly shows that a book was generated and identifies it as 9 pages.; The page has a clear cover, title, page indicator, and next-page control.; The story includes Sam by name on the cover, so the basic personalisation is visible.

### Hardcover checkout  (step 10)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** Show the complete cost of ordering the generated book as a hardcover and collect delivery and payment information.
- **What's happening:** The selected hardcover is £24.99, premium gift wrap is already checked at £7.99, shipping and handling is £12.99, and the displayed total is £45.97. Empty address and card fields appear below, along with an offscreen “Pay now” button.
- **First impression (Test):** "The breakdown is easy to see, but £45.97 feels high, and the pre-selected gift wrap makes the checkout feel a bit sneaky. I can see the base hardcover price, but I do not yet know the true delivered price without the optional add-on."
- **Cognitive walkthrough:** Q1 Yes, because my goal is to find out what the hardcover would really cost. I would not try to pay. / Q2 Yes, the checked “Premium gift wrap” checkbox is highly visible. / Q3 The checkout and order summary clearly concern the hardcover, but the checked optional add-on does not match what I asked to price.
  - [DECEPTIVE sev 3] **Optional gift wrap is selected by default** - evidence: [6] checkbox "Premium gift wrap" (checked), adding "£7.99". Fix: Make all optional extras unchecked by default and show the delivered hardcover total before asking the customer to opt in.
  - [VALUE sev 2] **The initial total does not plainly separate essential and optional costs** - evidence: "Hardcover: The Magical Adventrue of Sam £24.99", "Premium gift wrap £7.99", "Shipping & handling £12.99", "Total £45.97". Fix: Show "Hardcover", "Delivery", and "Optional extras" as separate groups, with a clear subtotal before optional add-ons and a final total after them.
  - [H4 sev 2] **The product title is inconsistent between the preview and checkout** - evidence: The preview was titled "The Magical Adventrue of Sam", while checkout says "Hardcover: The Magical Adventure of Sam".. Fix: Use the generated title consistently in the book preview, order summary, and checkout, and let the user correct it before ordering.
  - [CONTENT sev 1] **Hardcover is misspelled in the checkout title** - evidence: The order summary says "Hardcover: The Magical Adventrue of Sam". Fix: Correct “Adventrue” to “Adventure” everywhere, including the generated book title and checkout summary.
- **Positives:** The base hardcover price, gift wrap price, shipping charge, and total are all individually visible.; The checkout clearly identifies which book is being ordered.; A price-reservation countdown is visible.; The payment form is not pre-filled with sensitive information.

## Generated output assessment
*Artifact:* Nine-page personalized children's storybook preview with illustrations and a dedication page

> I can see that the website used Sam's name, age, the beach, and the yellow bucket, but the most important parts of my request are missing. Grandpa Joe and the sandcastles never appear, while an invented uncle and a frightening forest take over the story. The spelling errors, raw placeholders, mismatched pictures, wrong art style, and unfinished final sentence make the preview feel untrustworthy and not ready to buy.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The story uses Sam, age five, she/her, the beach, and a yellow bucket, but omits Grandpa Joe and the sandcastle-building event, misspells Sam as “Samn,” omits the supplied brown-haired appearance from the prose, replaces |
| coherence | 1 | The story jumps from sandcastles to abstract stargazing, rain, a lantern-bearing uncle, a frightening forest, and then home without explaining the transitions. Page 6 also says “he followed him,” contradicting Sam's esta |
| age fit | 1 | The supplied reading age is five, but Page 4 contains “ephemeral luminescence,” “crepuscular firmament,” “engendered,” “ineffable,” “juxtaposing,” and “existential trepidation.” The teeth-bearing shadows and suggestion t |
| language | 1 | Visible defects include “Adventrue,” “Samn,” “in the beach,” incorrect pronoun agreement, unresolved “{{recipient_name}}” and “{{sender_name}}” variables, duplicated story and ending text, and a final sentence without an |
| text image fit | 1 | Page 5 shows sunshine despite text describing pouring rain and puddles; Page 3 shows a yellow star instead of the yellow bucket; Page 6 lacks a clear lantern; Page 7 shows non-threatening trees and a balloon Sam is not h |
| character consistency | 2 | Sam is represented by a similar simple figure, but her hair changes from brown on the cover, Page 3, and Page 5 to black on Pages 4, 6, 7, 8, and 9. Grandpa Joe is never depicted, and the invented Uncle Bartholomew appea |
| visual quality | 1 | The illustrations are extremely sparse, reuse the same sun-water-land composition on several pages, and do not match the reported watercolour selection. Text labels appear awkwardly beneath characters, the cover title is |
| emotional resonance | 1 | The story does not meaningfully develop the specific shared memory of Sam building sandcastles with Grandpa Joe. Its unrelated magic, threatening forest, placeholder dedication, and unfinished ending make it feel generic |

- **used correctly:** Child's first name: Sam; Age: 5; Pronouns: she/her in most of the story; General appearance: Sam has brown hair on the cover and Pages 3 and 5; Setting: the beach is mentioned; Special object: a yellow bucket is mentioned
- **missing:** Grandpa Joe; The central event of building sandcastles; Any meaningful depiction of the yellow bucket in the illustrations; A watercolour-style illustration matching the reported selection; A completed sender or recipient dedication; Any verifiable evidence in the captured preview that Premium gift wrap was applied
- **changed:** The requested Grandpa Joe was replaced with Uncle Bartholomew; A gentle beach sandcastle memory was changed into an unrelated lantern and dark-woods adventure; Sam's hair changes inconsistently between brown and black; The title changes the generic idea of an adventure but misspells “Adventure”
- **invented:** Uncle Bartholomew; A lantern; A winding path; A deep dark forest; Shadows with teeth; The threat that no one would ever find Sam; A shiny red balloon; Sudden rain and Sam wearing a hood

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A simple pop-art-style scene with a small child labelled Sam, brown hair, a green shirt, a yellow star, a large sun, blue water, and a strip of green land. The title above the child visibly misspells “Adventure” as “Adventrue.”
- *Reaction:* The cover is readable, but the title error immediately makes it look unfinished. The picture is also much more primitive and pop-art-like than the watercolour style I apparently selected, and it does not show a beach memory with Grandpa Joe.
  - [language, sev 3] The title says “The Magical Adventrue of Sam”; “Adventrue” is misspelled.
  - [fidelity, sev 2] The cover does not mention Grandpa Joe, sandcastles, or the yellow bucket.
  - [visual_quality, sev 3] The cover states “Illustration style: Pop-art comic,” while the user's reaction identifies watercolour as the selected style.
  - [text_image_fit, sev 2] The image shows water, a sun, and a star but no sandcastle, Grandpa Joe, or yellow bucket to represent the requested beach memory.
- **Change I'd make:** Correct the title, use the selected watercolour style, and depict Sam and Grandpa Joe making a sandcastle with a yellow bucket on the beach.
- **Suggested rewrite:** The Magical Beach Adventure of Sam A StoryHearth original Illustration style: Watercolour

#### Dedication page
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A screenshot of page 2 in the StoryHearth preview interface. The white page contains unresolved template variables in italic text, with navigation controls and ordering controls visible around it.
- *Reaction:* This page looks like an unfinished template rather than a finished gift. The raw recipient and sender placeholders would be unacceptable in a paid keepsake.
  - [language, sev 4] The page visibly contains “{{recipient_name}}” and “{{sender_name}}.”
  - [fidelity, sev 3] No supplied recipient or sender information has been resolved into a personal dedication.
  - [visual_quality, sev 2] The dedicated page is essentially empty white space rather than a designed storybook page.
- **Change I'd make:** Replace both unresolved variables with finalized names. If the sender name is unavailable, use a complete non-placeholder dedication such as “For Sam, with love.”
- **Suggested rewrite:** For Sam, with love.

#### Page 3
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. Sam was 5 years old and loved nothing more than a yellow bucket.
- *Picture:* Sam stands alone beneath a large sun beside blue water and green ground. A yellow star-shaped object appears nearby, but there is no literal yellow bucket, Grandpa Joe, or sandcastle.
- *Reaction:* This introduces the right child, age, place, and object, but the wording is awkward and the picture fails to show the central family activity. Sam is also alone instead of with Grandpa Joe.
  - [language, sev 2] “In the beach” is ungrammatical; it should be “at the beach” or “on the beach.”
  - [fidelity, sev 4] The requested event was “A day at the beach building sandcastles with Grandpa Joe,” but no Grandpa Joe or sandcastle-building appears.
  - [text_image_fit, sev 3] The text names a yellow bucket, while the image shows a yellow star and no bucket.
  - [age_fit, sev 2] “There lived a curious child” and “loved nothing more” feel formal and unnecessary for a five-year-old's story.
- **Change I'd make:** Start the actual requested memory with Sam and Grandpa Joe using the yellow bucket to build a sandcastle, and draw those elements clearly.
- **Suggested rewrite:** Sam was five years old. On a sunny beach day, she and Grandpa Joe used her yellow bucket to build a wonderful sandcastle.

#### Page 4
![I4](artifacts/capture_05/img_00.jpg)
> One evening Sam gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Sam stands beneath a purple and pink evening sky dotted with a few white stars. There are no clouds, beach details, grandparents, bucket, or sandcastle.
- *Reaction:* The page jumps away from the beach memory into abstract adult prose that a five-year-old could not enjoy. The illustration is calm, but it does not continue the promised story.
  - [age_fit, sev 4] The sentence uses “ephemeral luminescence,” “crepuscular firmament,” “engendered,” “ineffable,” “juxtaposing,” and “existential trepidation.”
  - [coherence, sev 3] The sudden shift from building sandcastles to Sam alone gazing at an evening sky is not connected to the preceding events.
  - [text_image_fit, sev 2] The illustration gives only a generic evening sky and does not visually communicate the dense abstract sentence or the beach activity.
  - [fidelity, sev 2] Grandpa Joe, the sandcastles, and the yellow bucket disappear from the page's text and image.
- **Change I'd make:** Replace the abstract language with a concrete beach moment involving Sam, Grandpa Joe, the sandcastle, and the bucket.
- **Suggested rewrite:** The sun began to go down. Sam looked up at the pink sky and smiled. “Our castle looks just like a real castle!” she said.

#### Page 5
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Samn pulled up her hood and ran for shelter, holding a yellow bucket tight.
- *Picture:* The same simple daytime beach-like scene is repeated, with a bright sun, blue water, green ground, Sam, and a yellow star. There is no rain, puddle, hood, or visible bucket.
- *Reaction:* The typo “Samn” is obvious, and the picture shows sunshine while the text says heavy rain. It looks like a reused template image rather than an illustration of this page.
  - [language, sev 3] Sam is misspelled as “Samn.”
  - [text_image_fit, sev 4] The text says “rain began to pour” and “Big grey drops splashed into the puddles,” but the image has a bright sun and no rain or puddles.
  - [character_consistency, sev 2] Sam's hair is brown in this image, but it is black on several other pages.
  - [coherence, sev 2] Sam suddenly has a hood in a beach setting, and Grandpa Joe is absent when she runs away.
- **Change I'd make:** Correct Sam's name, show actual rain and puddles, or preferably keep the story focused on the sunny sandcastle memory with Grandpa Joe.
- **Suggested rewrite:** A few drops of rain began to fall. Sam held her yellow bucket tight while she and Grandpa Joe ran under the beach shelter.

#### Page 6
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Sam, follow me!" he called, and he followed him along the winding path.
- *Picture:* Sam stands beside a taller figure labelled Uncle Bartholomew near blue water. A small yellow rectangle appears beside the taller figure, but no lantern, winding path, beach details, or sandcastle are visible.
- *Reaction:* This is a major error: the person I supplied was Grandpa Joe, not Uncle Bartholomew. The pronoun also shifts from Sam to “he,” and the new character has no connection to the beach memory.
  - [fidelity, sev 4] The supplied person, “Grandpa Joe,” is replaced by the invented “Uncle Bartholomew.”
  - [coherence, sev 4] “He called, and he followed him” makes the grammatical subject Sam appear to be male, contradicting the supplied she/her pronouns.
  - [text_image_fit, sev 2] The text says Bartholomew appeared with a lantern, but the image shows only a small yellow rectangle and no clearly depicted lantern.
  - [character_consistency, sev 1] Uncle Bartholomew is invented and has no supplied appearance to compare against the story or image.
- **Change I'd make:** Remove Uncle Bartholomew and put Grandpa Joe in his place. Keep Sam's pronouns correct and show him helping with the sandcastle or bucket.
- **Suggested rewrite:** Grandpa Joe came along with his big hat. “Keep your yellow bucket safe, Sam,” he said. “We will use it for one last castle.

#### Page 7
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Sam again. Sam clutched a shiny red balloon and trembled in the dark.
- *Picture:* Sam stands at night near three simple trees, a crescent moon, stars, and a red balloon. The scene is dark but the shadows do not have teeth and the balloon is not visibly in Sam's hands.
- *Reaction:* This feels like an unrelated dark fantasy adventure and may frighten a five-year-old, especially with shadows that have teeth and the suggestion that Sam will never be found. Grandpa Joe and the beach memory have vanished again.
  - [fidelity, sev 4] The woods, red balloon, threatening shadows, and disappearance plot were not supplied and replace the requested sandcastle day.
  - [age_fit, sev 4] “The shadows grew teeth and whispered that no one would ever find Sam again” introduces unsettling horror imagery for a five-year-old.
  - [text_image_fit, sev 3] The image contains ordinary dark trees without teeth, and Sam is not visibly clutching the red balloon.
  - [coherence, sev 4] There is no explanation for why Sam left the beach, entered deep woods, became separated from Grandpa Joe, or acquired a balloon.
- **Change I'd make:** Replace the threatening forest scene with a gentle, causally connected beach scene in which Sam and Grandpa Joe finish or play with their sandcastle.
- **Suggested rewrite:** Sam and Grandpa Joe made one more castle together. Sam poured her yellow bucket carefully, and Grandpa Joe laughed when the sand piled up in a funny shape.

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. At last the sun came out, and Sam skipped all the way home, happier than ever.
- *Picture:* A nearly identical sunny blue-water scene is repeated, showing Sam, a yellow star, a large sun, green land, and no visible home, path, Grandpa Joe, sandcastle, or bucket.
- *Reaction:* The first sentence repeats the opening almost word for word, and the supposed resolution appears without explanation. The image is another reused sunny template rather than Sam going home after a meaningful day.
  - [coherence, sev 3] The first sentence duplicates Page 3: “Once upon a time, in the beach, there lived a curious child named Sam.”
  - [language, sev 2] “In the beach” is repeated and remains ungrammatical.
  - [text_image_fit, sev 3] The text says Sam “skipped all the way home,” but the picture shows her standing still in the same generic sun-and-water setting with no home or route.
  - [fidelity, sev 3] The ending does not resolve the requested day with Grandpa Joe or mention the sandcastles they made.
- **Change I'd make:** Remove the duplicated opening and show Sam and Grandpa Joe leaving the beach together after their sandcastle day, preferably carrying the bucket.
- **Suggested rewrite:** When they went home, Sam looked back at the sandcastle and smiled. She would always remember the special day she had built it with Grandpa Joe.

#### Page 9
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Sam looked up at the sky, she would always remember The End
- *Picture:* An orange background displays “The End” above Sam, who stands in the same green-and-blue landscape used throughout the book.
- *Reaction:* The ending repeats “The End” and stops in the middle of a sentence. It is not ready to print or give as a keepsake.
  - [language, sev 4] “She would always remember” has no object and no final punctuation.
  - [coherence, sev 3] “The End” appears both before and after the unfinished sentence.
  - [text_image_fit, sev 2] The page does not show the sky, beach memory, Grandpa Joe, or sandcastle that the final sentence refers to.
  - [emotional_resonance, sev 3] The incomplete final thought removes the natural place for a personal, keepsake-worthy memory of the day with Grandpa Joe.
- **Change I'd make:** Complete the final thought, name the shared memory with Grandpa Joe, remove the duplicate ending, and use a warmer closing image.
- **Suggested rewrite:** The End And from that day on, whenever Sam saw a yellow bucket, she would smile and remember building sandcastles with Grandpa Joe.

**Top changes to the output:** 1. Rebuild the story around Sam and Grandpa Joe building sandcastles with the yellow bucket at the beach. | 2. Remove Uncle Bartholomew, the dark forest, the teeth-bearing shadows, the disappearance threat, and the unrelated red balloon. | 3. Fix all text defects, including “Adventrue,” “Samn,” “in the beach,” pronoun agreement, duplicate passages, and the unfinished final sentence. | 4. Replace every raw dedication variable with finalized recipient and sender names before showing or purchasing the book. | 5. Regenerate unique watercolour illustrations that accurately show the yellow bucket, sandcastles, Grandpa Joe, and Sam's consistent brown hair. | 6. Rewrite the prose for a five-year-old using short, concrete sentences and remove advanced vocabulary and frightening imagery.

## Recommendations (participant's priorities)
- **[high] Rebuild the generated story around the actual memory: Sam and Grandpa Joe building sandcastles with the yellow bucket at the beach.** (Your storybook / book.html) - The central family memory was the whole point of making a personalised book, and it was almost entirely missing from the result.
- **[high] Remove the invented uncle, dark forest, threatening shadows, disappearance threat, and unrelated magical objects, or make any additions clearly appropriate and supportive of the submitted memory.** (Your storybook / book.html) - The story felt frightening and inappropriate for a five-year-old, and the invented content replaced my intended family moment.
- **[high] Regenerate unique watercolour illustrations that consistently show Grandpa Joe, sandcastles, the yellow bucket, the beach setting, and Sam's consistent brown hair.** (Your storybook / book.html) - The selected style was ignored, the artwork did not fit the memory, and the visual inconsistency made the book look cheap and unpolished.
- **[high] Add a clear review and edit step before purchase so I can confirm the child, character, memory, title, dedication, and illustration style in the final book.** (Create your book / create.html and Your storybook / book.html) - I had no confidence that the submitted details and family memory would actually be used correctly.
- **[high] Fix the spelling, grammar, pronoun, duplicate-text, placeholder-variable, and incomplete-ending errors throughout the generated book.** (Your storybook / book.html) - Typos and unfinished or unresolved text made the finished product look broken and unsuitable as a keepsake.
- **[high] Remove gift wrap as the default and show a simple itemised price for the essential hardcover, postage, and any optional extras before the final total.** (Checkout / checkout.html) - The initial £45.97 total was higher than I expected because an optional extra was selected without me choosing it.
- **[medium] Replace the raw dashboard error with a reassuring, understandable message that explains whether the account or book data is affected.** (My books / dashboard.html) - The technical error made me suspicious that my account data was incomplete or unsafe.
- **[medium] Replace the technical homepage phrase with plain language explaining that the site creates personalised illustrated stories.** (Homepage) - The multimodal generative narrative wording was unnecessarily confusing and made a family website sound like a sales pitch.
- **[medium] Add visible labels to the login fields, a persistent label for the photo upload, and stronger contrast for footer text and links.** (Log in / login.html and Create your book / create.html) - These accessibility and clarity issues made otherwise simple forms harder to trust and use.
- **[medium] Explain unfamiliar options such as the reading level and preselected choices in ordinary language, and confirm when character details have been saved.** (Create your book / create.html) - I did not understand what the reading level meant or whether details such as Grandpa Joe's appearance had been recorded.
- **[low] Make the story details field for the family memory more obvious on the first creation step, while clearly explaining the default relationship choice.** (Create your book / create.html) - I initially could not tell where the actual memory would be entered, and the automatic Grandparent relationship was unexpected.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is for creating and buying a personalised printed storybook based on a child's details and a family memory. It seems intended for parents or other family members wanting a keepsake for a young child.
- **What was the most frustrating or confusing moment, and why?** The worst moment was seeing the finished book after all the effort of entering the memory. It replaced the central sandcastle activity with Grandpa Joe with an invented uncle and frightening forest story, while also using the wrong illustration style and leaving an unfinished sentence.
- **What was the best moment?** The best part was entering the beach, yellow bucket, and memory of Sam building sandcastles with Grandpa Joe. That felt warm, personal, and exactly the sort of experience I hoped the site would create.
- **Was there any point where, in real life, you would have given up? Where and why?** In real life, I probably would not have abandoned the form at the checkout, but I would have stopped before paying when I saw that the output missed Grandpa Joe, the sandcastles, and the selected watercolour style. The £45.97 initial total with gift wrap already selected would also have made me hesitate.
- **What did you expect to find or be able to do that wasn't there?** I expected a coherent, polished story about Sam and Grandpa Joe building sandcastles at the beach, with matching watercolour illustrations and a complete ending. I also expected saved character details to be shown clearly and the final cost to separate the hardcover, postage, and optional extras plainly.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to enter the fictional child and family details, but I would not trust this site with sensitive family information. The raw error message on the dashboard, the inaccurate generated story, and the raw placeholder variables made me worry about how data was being stored and used.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would pay for a genuinely usable personalised keepsake, but not for this result. Around £25 to £30 including reasonable postage would feel fair, and I might pay more if the book accurately captured the requested memory, had consistent age-appropriate illustrations, and offered a clear editable preview before checkout.
- **If the site produced something for you, how do you feel about it overall?** The output felt generic, frightening, and completely untrustworthy rather than personal or keepsake-worthy. It was not ready for me to buy because it failed the basic purpose of the product.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | It looks warm and relevant to what I want, and the three steps are easy to understand. However, “Leverage our multimodal generative narrative engine” sounds far too technical and sales-like for a family website. I’m goin | click |
| 2 | Log in – StoryHearth | reassured (2) | This is clear and easy to scan. I can see exactly what I need to do, although the fields only have placeholders rather than visible labels. | type; type; click |
| 3 | My books – StoryHearth | confused (-1) | The login did work because I can see my account dashboard and a “Log out” link. But the raw error message makes me a bit suspicious and wonders whether my profile is actually complete. I’ll try creating a book and see if | click |
| 4 | Create your book – StoryHearth | curious (1) | This form is straightforward enough. I can see the fields clearly, and I’ll add Sam as the star, choose her age and pronouns, then add Grandpa Joe as the other character. The “Next” button is obvious, though I’m not yet  | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (1) | This step is easy to understand. I can enter the beach, the yellow bucket, and the memory about Sam building sandcastles with Grandpa Joe. I’m not sure whether Grandpa Joe’s grey hair was saved because I don’t see the ea | type; type; type; click |
| 6 | Create your book – StoryHearth | reassured (1) | The page looks neat and the choices are easy to scan. The selected reading level sounds right for Sam, and the soft watercolour style suits a family memory, though “Lexile” is jargon I don’t really understand. I’ll keep  | click |
| 7 | Create your book – StoryHearth | reassured (1) | This is simple and I understand that I can skip the photo. I don't have a suitable photo ready, so I’ll leave it empty and click “Create my book.” | click; wait_for_change |
| 8 | Your storybook – StoryHearth | confused (-1) | The book appeared, so the creation did work. I can see the title, cover, page count, and next arrow, but I’m confused by the spelling "Adventrue." More importantly, I expected a watercolour picture book about building sa | flip_through |
| 9 | Your storybook – StoryHearth | disappointed (-1) | I can see that the flip-through worked because the page count says 9 / 9 and the next arrow is disabled. The last page feels unfinished because the sentence stops after “remember”, and the pictures don’t look like the so | click |
| 10 | Checkout – StoryHearth | annoyed (-1) | That is more expensive than I expected, and I would not have expected “Premium gift wrap” to be selected by default. I want to find the cost of the actual hardcover without the optional extras, so I’ll untick gift wrap a | click; read_page |
| 11 | Checkout – StoryHearth | relieved (1) | That worked clearly: the gift-wrap checkbox is now empty and the total dropped from £45.97 to £37.98. The real cost is £24.99 for the hardcover plus £12.99 shipping and handling, with no gift wrap. I have what I came for | done |
