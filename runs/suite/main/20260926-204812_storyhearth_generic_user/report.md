# UserQA report: Test User on http://127.0.0.1:8765/

*Persona:* **Test User** (35) - Baseline condition - a generic adult web user with no persona conditioning (ablation).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 12 steps | *Pages reviewed:* 10 | *Issues:* 26 | *LLM calls:* 14 | *Wall time:* 372.9 s

## What the agent understood the website to be
- **what it is:** A website that creates personalised illustrated family storybooks from memories.
- **who it is for:** Families wanting a personalised story featuring their child and another loved one.
- **value proposition:** Turn a shared family memory into a digital storybook preview, with the option of a printed UK hardcover.
- **pricing model:** A free digital preview is advertised, with printed hardcovers sold separately; the actual price is not shown here.
- **fit for me:** Yes, this directly suits my goal of making and reading a story about Sam and Grandpa Joe before checking the hardcover cost.
- **main tasks:** Log in, Enter family characters and a memory, Generate and read the storybook, View the price of a printed hardcover

## Scores
- SUS: **32.5** (grade F; 68 = industry average)
- UEQ-S: pragmatic -1.25, hedonic 0.5 (range -3..+3)
- Likelihood to recommend (0-10): 1
- Output keepsake-worthiness (1-5): 1
- Verdict: *"Promising idea and a quick-looking preview, but too many serious personalisation, writing, visual, loading, and pricing problems for me to trust or pay for it."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Unexplained technical sync error | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-language message such as “We couldn’t fully load your profile. Try again or continue and check your details before printing,” and provide a working Retry control. |
| 3 | H5 | Choose look and feel | The memory was silently truncated | The result of entering field [18] said: “the box now only shows 200 characters; the end of what you typed was cut off”. | Add a visible character counter before the limit is reached, prevent further typing at the limit, and preserve the full entry while only displaying the permitted amount. |
| 3 | H1 | Book generation loading | Loading state has no explanatory status | A circular loading spinner is shown by itself inside the central panel, with no accompanying text. | Add a clear status message such as 'Creating Sam and Grandpa Joe's storybook…' and, if generation can take time, explain roughly how long it may take. |
| 3 | H2 | Generated storybook preview | Illustration style appears not to match my selection | The page says “Illustration style: Pop-art comic” even though I selected the Watercolour illustration style. | Ensure the selected style is carried through generation, and display the saved choice beside the preview with an option to correct it. |
| 3 | CONTENT | Generated storybook preview | Final page has an incomplete sentence | “And from that day on, whenever Sam looked up at the sky, she would always remember” | Complete the sentence with the beach memory, Grandpa Joe, and the sandcastles, and check all generated pages for incomplete grammar before presenting the preview. |
| 3 | DECEPTIVE | Hardcover checkout | Premium gift wrap is pre-selected | [6] checkbox "Premium gift wrap" (checked), with “£7.99” underneath | Make the gift-wrap checkbox unchecked by default and explain the added cost beside the option. Preserve the user’s choice while they adjust the order. |
| 2 | ACC | Log in, Create your book — characters (x2) | Footer links have very low contrast | In the screenshot, “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” appear extremely faint against the pale background. | Use darker footer text that meets WCAG contrast requirements, and make sure link states are clearly distinguishable. |
| 2 | CONTENT | StoryHearth homepage | Technical language makes the service sound unnecessarily complicated | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace this with plain wording such as: “Turn a treasured family memory into a beautifully illustrated storybook starring your loved ones.” |
| 2 | ACC | StoryHearth homepage | Hero illustration has no accessible description | The image is exposed as “[image (no description)]”. | Add concise alternative text describing the meaningful content of the illustration, or mark it decorative if it adds no information. |
| 2 | ACC | Log in | Login fields have placeholders instead of proper visible labels | [5] and [6] are described as “textbox (no label)” with placeholders “Email” and “Password” | Add persistent visible labels for “Email address” and “Password” above the fields, with programmatic labels associated with each input. |
| 2 | H1 | My books dashboard | No explanation of sync consequences | The warning only says “profile sync incomplete.” | State exactly what did not load, whether creation is affected, and whether the user should retry before continuing. |
| 2 | CONTENT | Create your book — characters | No appearance field for the second character | The page asks 'What do they look like? (optional)' only under the child's details, then moves straight to 'Who else is in the story?' | Add a clearly labelled optional 'What do they look like?' field under the second character's name and relationship. |
| 2 | CONTENT | Story details form | No way to provide Grandpa Joe's appearance | After asking "Who else is in the story?" and accepting "Grandpa Joe," this screen only offers "Where does the story happen?", "A special object", and "Tell us t | Add fields for each additional character's name, relationship, and appearance, or include Grandpa Joe in an editable character summary on this step. |
| 2 | H2 | Choose look and feel | Reading-level jargon is unexplained | The heading says “Reading level”, but every option is labelled with Lexile ranges such as [21] “Lexile BR–200L” and [22] “Lexile 200L–500L”. | Replace the jargon with familiar labels such as “First readers (ages 4–6)” and “Early chapter books (ages 6–8)”, with a short explanation and an age-based recommendation. |
| 2 | H6 | Choose look and feel | No personal age-based recommendation | Sam is age 5, but the page still has [22] “Lexile 200L–500L” selected and does not indicate that this may be too advanced. | Preselect and visibly explain the recommended option based on the child’s entered age, while still allowing me to change it. |

## Page-by-page
### StoryHearth homepage  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised family storybook service and direct visitors to creation, pricing, or login.
- **What's happening:** The landing page presents the service, a “Proceed” call to action, pricing and login links, a three-step process, testimonials, FAQ controls, and footer links.
- **First impression (Test):** "Warm and fairly easy to understand, but the main paragraph is overloaded with corporate and technical language. I can see what the site claims to do, although I would need to log in before creating anything."
- **Cognitive walkthrough:** Q1 Yes, because the site says it can turn a family memory into an illustrated storybook. / Q2 Yes, both “Proceed →” and the clearly labelled “Log in” control stand out at the top. / Q3 “Log in” exactly matches my immediate need to access my account. “Proceed →” is less explicit about whether it continues through login or starts a new story.
  - [CONTENT sev 2] **Technical language makes the service sound unnecessarily complicated** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with plain wording such as: “Turn a treasured family memory into a beautifully illustrated storybook starring your loved ones.”
  - [ACC sev 2] **Hero illustration has no accessible description** - evidence: The image is exposed as “[image (no description)]”.. Fix: Add concise alternative text describing the meaningful content of the illustration, or mark it decorative if it adds no information.
  - [H2 sev 1] **Proceed does not say whether login is required** - evidence: The primary button is labelled only “Proceed →” while a separate “Log in” link is in the header.. Fix: Label the button “Log in to create” when the visitor needs an account, or explain where it leads.
- **Positives:** “Log in” is prominent and immediately recognisable.; The three steps use concrete, plain language: “Tell us who”, “Share a memory”, and “We write & illustrate”.; “Free digital preview” makes it clear that I can inspect the result before considering a print.; The warm cream, brown, and orange visual design suits a family storybook.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Allow an existing StoryHearth customer to access the account and create or view a personalised storybook.
- **What's happening:** The login form is empty and ready for an email address and password. There is also a link to create a new account.
- **First impression (Test):** "The central login card is simple and easy to understand. I can tell what to do immediately, though the footer links look unusually washed out."
- **Cognitive walkthrough:** Q1 Yes, because I have been given an existing account and want to access it. / Q2 Yes, the two central text boxes and orange “Log in” button are immediately visible. / Q3 Yes. The “Email” and “Password” placeholders and “Log in” button match what I want, although persistent visible labels would be better.
  - [ACC sev 2] **Login fields have placeholders instead of proper visible labels** - evidence: [5] and [6] are described as “textbox (no label)” with placeholders “Email” and “Password”. Fix: Add persistent visible labels for “Email address” and “Password” above the fields, with programmatic labels associated with each input.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: In the screenshot, “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” appear extremely faint against the pale background.. Fix: Use darker footer text that meets WCAG contrast requirements, and make sure link states are clearly distinguishable.
  - [H3 sev 1] **No visible password recovery option** - evidence: The page offers “Log in” and “Create an account” but no “Forgot password?” link.. Fix: Add a clearly labelled “Forgot password?” link near the password field.
- **Positives:** The page has a clear “Welcome back” heading.; The email and password fields are large and easy to locate.; The primary “Log in” button is prominent and clearly labelled.; The layout is visually clean and does not distract from the login task.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the signed-in user’s saved books and provide a way to create a new one.
- **What's happening:** The account is signed in, no existing books are listed, and the user is prompted to create their first book, although a profile-sync warning is displayed.
- **First impression (Test):** "The main action is easy to spot, but the raw hexadecimal error is confusing and undermines my confidence that my account is fully working."
- **Cognitive walkthrough:** Q1 Yes, I would try creating a book despite the warning because the account page otherwise looks ready. / Q2 Yes, the orange “+ Create a new book” button is prominent and directly matches my goal. / Q3 Yes, “Create a new book” clearly tells me this will start making the personalised storybook.
  - [H9 sev 3] **Unexplained technical sync error** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-language message such as “We couldn’t fully load your profile. Try again or continue and check your details before printing,” and provide a working Retry control.
  - [H1 sev 2] **No explanation of sync consequences** - evidence: The warning only says “profile sync incomplete.”. Fix: State exactly what did not load, whether creation is affected, and whether the user should retry before continuing.
- **Positives:** The “+ Create a new book” control is prominent and clearly labelled.; The page directly confirms that the account is logged in and currently has no books.; The layout is simple and not cluttered.

### Create your book — characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect the main child and one other person who will appear in the personalised storybook.
- **What's happening:** The form is empty and ready for details about the child and another character. Age, pronouns, and relationship are unselected dropdowns, while the child's appearance is optional. The footer links and copyright are extremely faint.
- **First impression (Test):** "The main form looks neat and straightforward. It is reasonably clear what to enter, but the very pale footer is hard to see."
- **Cognitive walkthrough:** Q1 Yes, I would fill this in now because these are the people I want in the memory. / Q2 Yes, the labelled textboxes and dropdowns are visible, and the Next button is easy to notice. / Q3 Mostly. The labels describe what I need, but there is no appearance field for the other person even though the child has one.
  - [CONTENT sev 2] **No appearance field for the second character** - evidence: The page asks 'What do they look like? (optional)' only under the child's details, then moves straight to 'Who else is in the story?'. Fix: Add a clearly labelled optional 'What do they look like?' field under the second character's name and relationship.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: The footer shows 'Privacy', 'Terms', 'Contact' and '© 2026 StoryHearth Ltd.' in extremely faint text.. Fix: Use a darker, WCAG-compliant text colour while preserving the subdued footer style.
- **Positives:** The form is visually tidy and easy to scan.; The field labels clearly describe the main child and second character.; The Next button is prominent.; Optional appearance details are clearly marked as optional.

### Story details form  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, meaningful object, and family memory that will guide creation of the personalised book.
- **What's happening:** The form presents three empty fields for the story location, a special object, and a memory or idea, with navigation to the previous step or onward to the next step.
- **First impression (Test):** "The form looks clean and the prompts make sense, although the absence of a field for Grandpa Joe's appearance leaves me unsure whether that detail will carry into the book."
- **Cognitive walkthrough:** Q1 Yes, I can immediately describe the beach memory, choose the yellow bucket, and explain why the day mattered. / Q2 Yes, the three large fields and the orange "Next" button are easy to notice. / Q3 Yes, "Tell us the memory or idea behind your story" closely matches what I want to provide.
  - [CONTENT sev 2] **No way to provide Grandpa Joe's appearance** - evidence: After asking "Who else is in the story?" and accepting "Grandpa Joe," this screen only offers "Where does the story happen?", "A special object", and "Tell us the memory or idea behind your story".. Fix: Add fields for each additional character's name, relationship, and appearance, or include Grandpa Joe in an editable character summary on this step.
- **Positives:** The placeholders provide useful examples without making the fields feel rigid.; The prompts are short and written in ordinary family language.; The large fields and clear Back and Next controls make this step straightforward.

### Choose look and feel  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose an appropriate reading difficulty and visual illustration style for the personalised storybook.
- **What's happening:** The form shows four Lexile reading-level radio buttons and three illustration styles. The previously selected 200L–500L level and Watercolour style are checked, and the user can go back or continue.
- **First impression (Test):** "It looks neat and the illustration choices are understandable, but “Lexile” is jargon and there is no plain-language guidance for choosing the level for a five-year-old."
- **Cognitive walkthrough:** Q1 Yes, I need to choose a reading level and appearance before continuing. / Q2 Yes, the reading-level radio buttons and Next button are prominent. / Q3 Only partly. I want a book suitable for Sam at age 5, but the Lexile ranges do not plainly say which one to choose.
  - [H5 sev 3] **The memory was silently truncated** - evidence: The result of entering field [18] said: “the box now only shows 200 characters; the end of what you typed was cut off”.. Fix: Add a visible character counter before the limit is reached, prevent further typing at the limit, and preserve the full entry while only displaying the permitted amount.
  - [H2 sev 2] **Reading-level jargon is unexplained** - evidence: The heading says “Reading level”, but every option is labelled with Lexile ranges such as [21] “Lexile BR–200L” and [22] “Lexile 200L–500L”.. Fix: Replace the jargon with familiar labels such as “First readers (ages 4–6)” and “Early chapter books (ages 6–8)”, with a short explanation and an age-based recommendation.
  - [H6 sev 2] **No personal age-based recommendation** - evidence: Sam is age 5, but the page still has [22] “Lexile 200L–500L” selected and does not indicate that this may be too advanced.. Fix: Preselect and visibly explain the recommended option based on the child’s entered age, while still allowing me to change it.
- **Positives:** The selected radio buttons and their current state are easy to see.; The illustration-style descriptions are warm, concrete, and easy to compare.; The form has a clear Back and Next action.

### Optional photo upload  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Offer an optional child photo to personalise the illustrations, then allow the user to create the book.
- **What's happening:** This is the last step of the creation flow. The user can upload a clear image of Sam’s face or proceed without one using “Create my book.”
- **First impression (Test):** "I can see this is optional and understand why a photo might help, so I’m happy to skip it and create the book."
- **Cognitive walkthrough:** Q1 Yes, I would create the book without a photo because the upload is optional. / Q2 Yes, the file chooser and the “Create my book” button are both visible. / Q3 Mostly. “Create my book” clearly matches what I want, but “Choose file” does not explicitly identify whose photo this is or what kind of image to choose.
  - [ACC sev 2] **File control lacks a specific visible label** - evidence: [30] file-upload (no label) and “Choose file \| No file chosen”. Fix: Add a proper visible and accessible label, such as “Sam’s photo (optional),” to the file input.
  - [TRUST sev 2] **Photo privacy and deletion are not explained** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.”. Fix: Add a short note stating how the photo is used, whether it is retained, and when it is deleted, with a link to the full privacy policy.
- **Positives:** The heading and explanatory sentence clearly say that the photo is optional.; The primary “Create my book” button is prominent.; A Back button is available, so this step is easy to reverse.

### Book generation loading  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** To show that the submitted story details are being used to generate the personalised book.
- **What's happening:** The page contains a bordered panel with a circular loading indicator, while the standard navigation and footer remain visible.
- **First impression (Test):** "At first this looks like a blank processing screen with an unexplained spinner. I do not know whether generation is underway or whether the page has stalled."
- **Cognitive walkthrough:** Q1 Yes, but only for a short while; I would wait to see whether the finished book appears. / Q2 I notice the spinner, but there is no explicit control, such as Cancel, on this screen. / Q3 No. There is no label or status message, so the spinner does not clearly tell me that my book is being generated.
  - [H1 sev 3] **Loading state has no explanatory status** - evidence: A circular loading spinner is shown by itself inside the central panel, with no accompanying text.. Fix: Add a clear status message such as 'Creating Sam and Grandpa Joe's storybook…' and, if generation can take time, explain roughly how long it may take.
  - [H3 sev 2] **No way to stop or leave while processing** - evidence: The central panel contains only the spinner, with no visible Cancel, Back, or edit control.. Fix: Keep a Back or My books control available, and offer a Cancel generation option with a clear confirmation.
- **Positives:** The large spinner makes it clear that the page is doing some work.; Navigation remains visible, so the layout does not appear to have crashed completely.

### Generated storybook preview  (step 9)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** To show the generated 9-page storybook and provide controls for reading its pages, regenerating the book, or ordering a hardcover.
- **What's happening:** A generated preview is open on page 1 of 9. The cover is titled “The Magical Adventrue of Sam,” the page indicator shows 1 / 9, and the next-page arrow is available while the previous-page arrow is disabled. The page also identifies the illustration style as “Pop-art comic.”
- **First impression (Test):** "The book is clearly presented and easy to open, but I immediately noticed the misspelling “Adventrue” and the fact that the style is “Pop-art comic” rather than the watercolour style I selected. That makes me uncertain whether my choices were applied correctly."
- **Cognitive walkthrough:** Q1 Yes, because I need to read the whole generated book carefully. / Q2 Yes, I can see the right-arrow button and the “1 / 9” page indicator; the regeneration and hardcover controls are visible after scrolling. / Q3 The next-page arrow clearly matches moving forward through the book, but the cover title and illustration-style label do not match the content I expected.
  - [H2 sev 3] **Illustration style appears not to match my selection** - evidence: The page says “Illustration style: Pop-art comic” even though I selected the Watercolour illustration style.. Fix: Ensure the selected style is carried through generation, and display the saved choice beside the preview with an option to correct it.
  - [CONTENT sev 3] **Final page has an incomplete sentence** - evidence: “And from that day on, whenever Sam looked up at the sky, she would always remember”. Fix: Complete the sentence with the beach memory, Grandpa Joe, and the sandcastles, and check all generated pages for incomplete grammar before presenting the preview.
  - [CONTENT sev 2] **Generated title contains a spelling error** - evidence: “The Magical Adventrue of Sam”. Fix: Add a spelling check before displaying the generated title, or let the user edit the title before saving.
  - [H1 sev 2] **No explanation of generation or choices applied** - evidence: The page changes from an unexplained loading state directly to the preview and only shows “Illustration style: Pop-art comic.”. Fix: Show a generation-complete message and a concise summary of the hero, supporting character, memory, reading level, and illustration style used.
- **Positives:** The generated output is presented in a clear book-like layout.; The page indicator and forward arrow make it obvious that this is page 1 of 9.; The preview is available without requiring payment.

### Hardcover checkout  (step 11)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** Show the hardcover order total, optional extras, delivery details, payment fields, and the final payment action.
- **What's happening:** The page displays the selected book “The Magical Adventrue of Sam,” its £24.99 price, £12.99 shipping and handling, a checked £7.99 premium gift-wrap add-on, and a total of £45.97. The address and payment form is ready for entry, and the page states that the price is reserved for 09:57.
- **First impression (Test):** "The price breakdown is easy to see, but I’m suspicious that gift wrap has been selected by default. I would not want to pay for it unless I had deliberately chosen it."
- **Cognitive walkthrough:** Q1 I would try to remove the pre-selected gift wrap so I could see the real basic cost. / Q2 Yes, I noticed the checked “Premium gift wrap” checkbox. / Q3 Yes, “Premium gift wrap” matches what it adds, but the fact that it is pre-ticked is not clearly explained.
  - [DECEPTIVE sev 3] **Premium gift wrap is pre-selected** - evidence: [6] checkbox "Premium gift wrap" (checked), with “£7.99” underneath. Fix: Make the gift-wrap checkbox unchecked by default and explain the added cost beside the option. Preserve the user’s choice while they adjust the order.
  - [VALUE sev 2] **Basic price is not obvious next to the total** - evidence: “Hardcover: The Magical Adventrue of Sam £24.99”, “Shipping & handling £12.99”, “Total £45.97”. Fix: Show a clearly labelled subtotal for hardcover and shipping before optional extras, then show the gift-wrap charge and final total.
  - [DECEPTIVE sev 2] **Unclear time-limited price reservation** - evidence: “Your price is reserved for 09:46”. Fix: Say exactly what the timer means and when it started, for example: “Your price is held until 09:46 on 12 June.” Avoid urgency wording unless the offer genuinely expires.
  - [TRUST sev 1] **Payment form asks for sensitive information before order review** - evidence: The visible form includes “Card number”, “Expiry”, and “CVC”, followed by a “Pay now” button.. Fix: Keep the price summary prominent, avoid presenting the payment form as the main next step, and make the privacy and security information easy to find before payment.
- **Positives:** The hardcover title and individual charges are shown clearly.; The total is visible near the top of the checkout.; There is a visible privacy link near the payment area.

## Generated output assessment
*Artifact:* AI-generated nine-page personalized children's story preview with an online checkout

> I was pleasantly surprised that the site produced a complete nine-page preview, but reading it made the basic errors obvious. It feels like a generic dark adventure rather than a keepsake about Sam and Grandpa Joe, and the placeholders, misspellings, unrelated pictures, and unfinished ending would make the result untrustworthy. I would want a complete regeneration and proof check before considering an order.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The name Sam, age five, she/her pronouns, beach, and yellow bucket appear, and the drawings broadly use a brown-haired child. However, "Grandpa Joe" appears zero times; the sandcastles, his grey hair becoming sandy, the  |
| coherence | 2 | There is a nominal beginning, middle, and end, but the beach story abruptly becomes a dark adventure involving an invented uncle. The opening sentence is repeated on page 8, the shadows are never resolved, and the final  |
| age fit | 1 | The measured Flesch-Kincaid grade is 6.9 for a requested reading age of five, and the page containing "ephemeral luminescence of the crepuscular firmament" is far beyond the target. The line about toothy shadows saying n |
| language | 1 | Unresolved "{{recipient_name}}" and "{{sender_name}}" placeholders remain, "Adventure" is misspelled as "Adventrue," Sam becomes "Samn," "in the beach" is incorrect, the opening is repeated, and the final sentence is cut |
| text image fit | 2 | Several pages broadly illustrate their headings, but I5 shows sun instead of pouring rain, I3 and I8 omit the yellow bucket and Grandpa Joe, I6 shows the beach rather than a winding path, and the toothy whispering shadow |
| character consistency | 3 | The simple green-shirted child is broadly consistent across most pages and has short brown colouring that loosely matches the input. However, the character is not clearly depicted as a girl despite the she/her input, and |
| visual quality | 2 | The colours are clean and there are no obvious extra fingers or distorted faces, but the artwork is extremely sparse and generic, labels such as "Sam" sit awkwardly on the ground, several scenes are reused, and I4 contai |
| emotional resonance | 1 | Despite the supplied happy memory of Sam and Grandpa Joe laughing and working together, the book centres on melancholy, rain, frightening woods, and an invented uncle. The unfinished final sentence prevents a meaningful  |

- **used correctly:** The child's first name, Sam, is used consistently in most places.; The age five is stated in the opening.; The she/her pronouns are maintained where pronouns are used.; The beach setting is mentioned and frequently illustrated.; The yellow bucket is mentioned in the story.; A short brown-haired child is depicted with reasonable visual consistency.; No email address or password was exposed in the generated book or checkout.
- **missing:** Grandpa Joe appears zero times and is not illustrated.; Building sandcastles together is missing.; Grandpa Joe's grey hair getting sandy is missing.; The sea breeze is missing.; Sam laughing and working together with Grandpa Joe is missing.; The central happy-day memory is not carried through.; The requested BR–200L reading level is not met; the measured grade level is 6.9.; The selected premium gift wrap is not correctly reflected in the checkout state or total.
- **changed:** The requested happy family beach day was changed into a sombre fantasy adventure.; The trusted family relationship with Grandpa Joe was omitted.; The plain-vector artwork is described as "Pop-art comic" but is not developed as a comic-style sequence.; The requested gift-wrap configuration appears to have been dropped at checkout.
- **invented:** Uncle Bartholomew; a lantern and winding path; rain and Sam running for shelter; a lonely evening and existential melancholy; dark woods with shadows that grow teeth; a threat that no one will ever find Sam; a shiny red balloon

### Part by part
#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A sparse, flat-colour illustration of a small brown-haired child labelled "Sam," standing between blue water and a green shoreline. A large sun and yellow star appear beneath the title "The Magical Adventrue of Sam."
- *Reaction:* The simple cover is easy to read, but the misspelled title immediately makes it feel careless. It also does not show the family beach memory that was requested.
  - [language, sev 3] The title says "The Magical Adventrue of Sam"; "Adventure" is misspelled as "Adventrue."
  - [fidelity, sev 3] The cover shows only Sam and a generic shoreline, with no Grandpa Joe, yellow bucket, sandcastles, or shared activity.
  - [visual_quality, sev 2] The image is very sparse and resembles a simple vector placeholder rather than a polished pop-art comic, despite the label "Illustration style: Pop-art comic."
- **Change I'd make:** Correct "Adventure," use a title centred on the real memory, and illustrate Sam and Grandpa Joe building a sandcastle with the yellow bucket.
- **Suggested rewrite:** The Magical Beach Day with Grandpa Joe A StoryHearth original Illustration style: Pop-art comic

#### Page 2 / Dedication
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A mostly blank white book page displays the unresolved dedication in italics. The surrounding website preview also repeats the misspelled book title and shows the page indicator "2 / 9."
- *Reaction:* Leaving raw template placeholders on a paid personalized book is a basic failure. It looks unfinished rather than personal.
  - [language, sev 4] The page visibly contains "{{recipient_name}}" and "{{sender_name}}" instead of names.
  - [fidelity, sev 3] No recipient or sender was supplied, yet the site has not removed or safely adapted the dedication fields.
  - [language, sev 3] The surrounding preview heading again shows "The Magical Adventrue of Sam."
- **Change I'd make:** If no recipient or sender is available, print only a suitable generic dedication; otherwise replace both placeholders with validated names and test for unresolved braces before checkout.
- **Suggested rewrite:** For Sam, with love from her family

#### Page 3 / Page 1
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. Sam was 5 years old and loved nothing more than a yellow bucket.
- *Picture:* Sam stands alone in a very simple green shirt and dark trousers beneath a large sun. A blue strip of water and a yellow star are visible, but there is no bucket, sandcastle, or second person.
- *Reaction:* Sam's name and age are present, but this does not feel like the family day I described. The missing Grandpa Joe and bucket make the opening feel like a different story.
  - [fidelity, sev 4] "Grandpa Joe" is absent, and the requested event of Sam and Grandpa Joe building sandcastles together never begins.
  - [language, sev 2] "in the beach" is ungrammatical; standard wording is "at the beach."
  - [text_image_fit, sev 3] The text says Sam loves a yellow bucket, but no yellow bucket appears in I3.
  - [character_consistency, sev 2] The child has short brown hair, but the plain green shirt and trousers do not clearly establish Sam as a girl despite the requested "she/her" pronouns.
- **Change I'd make:** Open with Sam and Grandpa Joe at the beach, and show both of them using the yellow bucket to build a sandcastle.
- **Suggested rewrite:** Sam was five years old. On a sunny day at the beach, she and Grandpa Joe built sandcastles together. They used a yellow bucket to carry the sand.

#### Page 4 / Page 2
![I4](artifacts/capture_05/img_00.jpg)
> One evening Sam gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Sam stands front-facing under a purple and pink evening sky with small white stars. A dark square-like artefact is partly visible near the sun.
- *Reaction:* This vocabulary is far beyond a five-year-old and sounds artificially elaborate. The sudden melancholy also changes the happy family memory into something sombre.
  - [age_fit, sev 4] The sentence uses "ephemeral," "luminescence," "crepuscular firmament," "engendered," "melancholy," "juxtaposing," "ineffable," and "existential trepidation." The measured grade level was 6.9 rather than the requested age 5 level.
  - [fidelity, sev 4] The supplied memory was a "happy day" involving Grandpa Joe, laughter, and working together, not a solitary evening filled with melancholy.
  - [coherence, sev 3] The story changes from a sunny beach introduction to "One evening" without explaining what happened in between.
  - [text_image_fit, sev 2] The sky and evening colours broadly fit the text, but Sam is standing straight ahead rather than "gazed upward," and I4 contains a dark blocky artefact near the sun.
- **Change I'd make:** Replace the sentence with concrete, age-appropriate beach action involving Grandpa Joe, and regenerate the image without the square artefact.
- **Suggested rewrite:** Sam looked up at the blue sky. A soft sea breeze blew through Grandpa Joe's grey hair while they worked together.

#### Page 5 / Page 3
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Samn pulled up her hood and ran for shelter, holding a yellow bucket tight.
- *Picture:* The image repeats the sunny daytime beach scene with Sam, the sun, yellow star, green shore, and blue water. Sam has no visible hood, there are no raindrops or puddles, and no bucket is shown.
- *Reaction:* The name error is obvious, and the picture directly contradicts the rainy weather. This is the kind of mistake that would make me distrust the rest of the book.
  - [language, sev 4] The story spells Sam's name as "Samn."
  - [text_image_fit, sev 4] The text describes pouring rain, grey drops, puddles, and a hood, while I5 shows a bright sun, no rain, no puddles, and no hood.
  - [fidelity, sev 3] Although the yellow bucket is mentioned, it is not illustrated, and Grandpa Joe and the sandcastle-building memory remain absent.
  - [coherence, sev 3] Sam runs away from the beach without the trusted adult requested in the story, beginning a sudden and unexplained adventure.
- **Change I'd make:** Correct the name and show a light, age-appropriate beach mishap or shared game rather than replacing the day with a rainy flight.
- **Suggested rewrite:** Sam held her yellow bucket tight. Grandpa Joe helped her scoop up the sand that spilled, and they laughed as they filled the bucket again.

#### Page 6 / Page 4
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Sam, follow me!" he called, and he followed him along the winding path.
- *Picture:* A larger adult labelled "Uncle Bartholomew" stands beside Sam with a small yellow rectangle that may represent a lantern. They remain in the same flat shoreline setting, with no visible winding path.
- *Reaction:* This introduces an important person who was never mentioned and removes the grandfather at the centre of the memory. The last sentence is also confusing because both people use "him."
  - [fidelity, sev 4] The requested relative, "Grandpa Joe," is replaced by the invented character "Uncle Bartholomew."
  - [language, sev 3] "Sam, follow me!" he called, and he followed him along the winding path" leaves the pronoun references unclear and sounds as though Uncle Bartholomew may be following Sam.
  - [coherence, sev 3] Uncle Bartholomew appears suddenly and redirects Sam away from the beach without a clear connection to the previous event.
  - [text_image_fit, sev 2] I6 includes Bartholomew and a possible lantern, but the surrounding image is still the beach and does not show the stated winding path.
- **Change I'd make:** Delete Uncle Bartholomew and replace the whole sequence with Grandpa Joe helping Sam continue building at the beach.
- **Suggested rewrite:** Grandpa Joe showed Sam how to make a wide wall for the sandcastle. Sam copied him, and soon they had built a tall tower together.

#### Page 7 / Page 5
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Sam again. Sam clutched a shiny red balloon and trembled in the dark.
- *Picture:* Sam stands alone at night near three simple trees, a crescent moon, stars, and a floating red balloon. No toothed shadows, whispering figures, or Grandpa Joe are shown.
- *Reaction:* This is noticeably frightening for Sam's age, especially because she is alone and the supplied memory was happy. The red balloon appears, but it has no connection to the beach day I requested.
  - [age_fit, sev 3] "The shadows grew teeth" and "no one would ever find Sam again" introduce a threatening, disappearance-related fantasy that may be too frightening for a five-year-old.
  - [coherence, sev 3] The story jumps from a beach and winding path to "Deep in the woods" without establishing why Sam went there or how the trusted adult would respond.
  - [fidelity, sev 4] The red balloon and threatening woods are invented, while Grandpa Joe, the sandcastles, the sea breeze, and the shared laughter are still missing.
  - [text_image_fit, sev 2] The night woods and red balloon fit generally, but I7 does not show teeth on the shadows or indicate that they are whispering.
- **Change I'd make:** Remove the threatening woods entirely and return to a safe, positive scene of Sam and Grandpa Joe working and laughing together.
- **Suggested rewrite:** Sam and Grandpa Joe carried their yellow bucket to the water. They filled it with warm sand and made one more castle before it was time to go home.

#### Page 8 / Page 6
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. At last the sun came out, and Sam skipped all the way home, happier than ever.
- *Picture:* The cover's generic sunny beach image is reused almost exactly, with Sam standing alone beneath the sun and star. There is no homeward movement, Grandpa Joe, yellow bucket, or sandcastle.
- *Reaction:* Repeating the opening after the dark-woods scene makes the story feel assembled from unrelated pieces. It also skips the family moment that should make the ending meaningful.
  - [coherence, sev 4] "Once upon a time, in the beach, there lived a curious child named Sam" repeats the opening after Sam has already left the beach and entered the woods.
  - [fidelity, sev 4] The supposedly happy ending does not mention Grandpa Joe, their sandcastles, the yellow bucket, Grandpa's sandy grey hair, or the laughter and teamwork supplied in the memory.
  - [text_image_fit, sev 3] The text says Sam "skipped all the way home," but the image shows her standing still in the same generic shoreline scene used earlier.
  - [language, sev 2] The phrase "in the beach" is repeated, and "the sun came out" is not connected to the earlier unexplained rain.
- **Change I'd make:** Do not restart the story. End the actual sandcastle episode with Sam and Grandpa Joe packing up and remembering their shared laughter.
- **Suggested rewrite:** When their sandcastles were ready, Sam and Grandpa Joe smiled at their work. Grandpa Joe's grey hair was sandy, and Sam laughed as she carried the yellow bucket home.

#### Page 9 / Page 7
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Sam looked up at the sky, she would always remember The End
- *Picture:* An orange page shows one large "The End" heading above the same generic, front-facing child standing by the blue water and green shore.
- *Reaction:* The final thought stops in the middle of a sentence, which feels broken. "The End" also appears twice in the captured page text, and the image does not capture the family memory.
  - [language, sev 4] The sentence ends at "she would always remember" with no object or final punctuation, and "The End" appears both before and after the unfinished sentence.
  - [coherence, sev 4] The intended final memory is incomplete, so the story does not provide a clear emotional resolution.
  - [fidelity, sev 4] The final sentence never identifies what Sam remembered, losing the central detail that she remembered laughing and working together with Grandpa Joe.
  - [text_image_fit, sev 2] I9 matches the standalone "The End" label, but it shows neither Grandpa Joe nor sandcastles and does not illustrate Sam remembering the day.
  - [emotional_resonance, sev 3] A solitary placeholder figure and an incomplete sentence do not create a personal or keepsake-worthy closing moment.
- **Change I'd make:** Complete the memory, remove the duplicate ending, and show Sam and Grandpa Joe together beside their sandcastles in the final image.
- **Suggested rewrite:** The End From that day on, whenever Sam looked at the sea, she remembered laughing and building sandcastles with Grandpa Joe.

#### Checkout
![I10](artifacts/capture_12/view_00.jpg)
![I11](artifacts/capture_12/view_01.jpg)
> Checkout Your price is reserved for 09:36 Hardcover: The Magical Adventrue of Sam	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£37.98 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* A clean checkout page shows the hardcover and shipping prices, a £7.99 premium gift-wrap option with an apparently empty checkbox, empty delivery and payment fields, and an orange "Pay now" button.
- *Reaction:* I would be wary of paying because the selected gift wrap does not appear to be applied. The displayed total is also wrong if the requested gift wrap is included, and the misspelled title is carried into checkout.
  - [fidelity, sev 3] Premium gift wrap was selected, but its checkbox appears empty and the £37.98 total equals only £24.99 plus £12.99 shipping, excluding the £7.99 gift wrap.
  - [language, sev 3] Checkout repeats "The Magical Adventrue of Sam," and the arithmetic is inconsistent: £24.99 + £7.99 + £12.99 equals £45.97, not £37.98.
  - [visual_quality, sev 2] The checkout layout is clean, but the selected-option state and total are unclear, which creates a risk of charging for the wrong configuration.
- **Change I'd make:** Preserve the selected gift-wrap state, show a checked box, calculate the total as £45.97, and block ordering until the title and preview pass automated checks.
- **Suggested rewrite:** Checkout Your price is reserved for [remaining time] Hardcover: The Magical Beach Day with Grandpa Joe — £24.99 Premium gift wrap — selected — £7.99 Shipping & handling — £12.99 Total — £45.97 Delivery Address Payment Card number Expiry CVC Pay now

**Top changes to the output:** 1. Rebuild the entire story around Sam and Grandpa Joe building sandcastles together with the yellow bucket. | 2. Remove the invented uncle, dark woods, toothy shadows, lantern adventure, red balloon, melancholy, and disappearance language. | 3. Replace all advanced vocabulary and retest the finished book to a suitable early-reader level near BR–200L. | 4. Correct "Adventrue," "Samn," "in the beach," the repeated opening, and the unfinished final sentence; block checkout on unresolved placeholders or truncation. | 5. Regenerate the illustrations so Grandpa Joe appears consistently with grey hair, Sam is clearly a brown-haired girl, the bucket and sandcastles are visible, and each picture matches its page. | 6. Complete the final memory around laughing and working together, and present "The End" only once. | 7. Make the selected premium gift wrap visibly checked and correct the total to £45.97 before accepting payment.

## Recommendations (participant's priorities)
- **[high] Rebuild the story around the supplied memory, including Sam, Grandpa Joe, the beach, the yellow bucket, and building sandcastles together.** (Generated storybook preview and generation logic) - Personalisation is the entire point of the product, and the current output omitted the most important relationship and events.
- **[high] Remove invented dark-adventure content such as Uncle Bartholomew, threatening shadows, rain, woods, the lantern, and the red balloon unless it is actually based on the user's story.** (Generated storybook preview) - The unexpected dark and frightening material does not match the happy family memory and may not be appropriate for a young child.
- **[high] Make the final page a complete, meaningful ending that resolves the beach memory and includes “The End” only once.** (Generated storybook preview) - The unfinished sentence makes the book look broken and prevents it from feeling like a keepsake.
- **[high] Correct spelling and language errors, remove unresolved template placeholders, repeated text, truncation, and grammar mistakes, and prevent checkout until automated checks pass.** (Generated storybook preview and checkout) - These visible defects made the story look unprofessional and made me unwilling to pay.
- **[high] Add appearance fields for every important character, including Grandpa Joe, and carry those descriptions into the illustrations consistently.** (Create your book — characters and Story details form) - I could describe Sam but had no way to record Grandpa Joe's grey hair or ensure he appeared in the finished book.
- **[high] Regenerate illustrations so Grandpa Joe appears, Sam is clearly a brown-haired girl, the yellow bucket and sandcastles are visible, and each image matches its page.** (Generated storybook preview) - The current pictures were sparse, reused, sometimes mismatched, and did not support the story.
- **[high] Explain the book-generation state, show what is happening, and provide a safe way to leave or retry without losing entered information.** (Book generation loading) - The blank loading experience left me unsure whether to wait, go back, or refresh.
- **[high] Explain reading levels in plain language and recommend a suitable range based on the child's age, while still allowing me to choose another range.** (Choose look and feel) - I did not know what Lexile meant or which range was appropriate for a five-year-old.
- **[high] Show the basic book price, shipping, gift wrap, taxes, and total separately, and do not preselect premium gift wrap.** (Hardcover checkout) - The £45.97 total was surprising, and an unwanted add-on was already selected when I arrived.
- **[medium] Clarify exactly when a reserved price expires and what happens if the timer expires.** (Hardcover checkout) - The countdown felt pressuring because the site did not explain what was being reserved or when the offer would end.
- **[medium] Add proper visible labels, password recovery, stronger footer contrast, and a specific label for the photo upload.** (Log in, homepage, and Optional photo upload) - Placeholders, faint footer text, and an unlabelled file control made basic tasks less accessible and less clear.
- **[medium] Explain photo privacy, storage, and deletion, and explain any sync errors instead of displaying technical wording.** (Log in, Optional photo upload, and My books dashboard) - Unclear data handling and unexplained errors would make me hesitant to provide family photos or personal information.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is a website for creating personalised children's storybooks featuring a child and other people they care about. It seems aimed mainly at parents or family members who want a keepsake story rather than just a generic children's book.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the finished book ignore Grandpa Joe and the beach memory, then display a generic dark adventure with the wrong illustration style, spelling mistakes, unresolved placeholders, and an unfinished ending. The unexplained generation screen was also confusing, but the broken final result felt much worse.
- **What was the best moment?** The best moment was seeing that the site had actually generated a complete nine-page preview. The beginning was easy to understand and the idea of making a story starring Sam was exciting, even though the result did not meet my expectations.
- **Was there any point where, in real life, you would have given up? Where and why?** Yes. I would seriously consider giving up after reading the generated book, because it did not use the most important person in the story and was not presentation-ready. I would probably also pause at checkout, since the price was much higher than expected and premium gift wrap had been selected without me asking for it.
- **What did you expect to find or be able to do that wasn't there?** I expected fields for describing Grandpa Joe's appearance, such as his grey hair, and a way to include him consistently in the story and illustrations. I also wanted a clear reading-level recommendation for a five-year-old, a labelled and privacy-explained photo upload, useful loading status, a complete review of the story before ordering, and an obvious explanation of the price and reservation deadline.
- **Did you trust this website with your information (and your family's)? Why or why not?** I would not yet trust the site with payment or sensitive family photos. The unexplained sync message, unclear photo handling, silent truncation, and inaccurate output made me worry that the site was not handling my information or choices reliably.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would not pay for this version. Even for a well-made personalised hardcover, I would expect around £25-£30, with any gift wrap, shipping, and other extras shown separately before checkout. I might pay more if the book accurately featured Sam and Grandpa Joe, had excellent age-appropriate language and illustrations, and included a clear proof before payment.
- **If the site produced something for you, how do you feel about it overall?** I was pleasantly surprised that a complete preview appeared, but the finished book felt like a generic dark adventure rather than a personal keepsake. The missing Grandpa Joe, frightening and unrelated content, wrong style, spelling errors, unresolved placeholders, mismatched pictures, and incomplete ending would make me distrust the product and regenerate it rather than order it.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This looks relevant to what I want, though “Leverage our multimodal generative narrative engine” sounds far more technical and sales-like than the simple idea of making a family storybook. The three steps are easy to und | click |
| 2 | Log in – StoryHearth | reassured (1) | This is straightforward and I know my account details, so I’ll fill these in and log in. The form looks clean, although the footer text is very faint. | type; type; click |
| 3 | My books – StoryHearth | confused (0) | I’m logged in, so that’s clear enough, but this error message is strange and technical. I don’t know whether my profile is actually incomplete or whether this will affect the book, but I can still try creating one. | click |
| 4 | Create your book – StoryHearth | neutral (1) | This form is clear enough and fits what I want. I can put Sam in as the hero and add Grandpa Joe, although I notice there isn't yet a place to say what Grandpa Joe looks like. | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | confused (1) | This is easy to understand and the placeholders are helpful. I can describe our day at the beach, including the yellow bucket, but I still can't add Grandpa Joe's grey hair here. | type; type; type; click |
| 6 | Create your book – StoryHearth | confused (0) | I can see the choices, but I don’t know what Lexile means or which range is right for a five-year-old. I’ll choose the “BR–200L” option because that sounds most like a beginner reader, keep the pretty watercolour style,  | click; click |
| 7 | Create your book – StoryHearth | reassured (1) | This last step is simple, but the file control is just the browser’s “Choose file” button and doesn’t explicitly say whose photo it wants. I’ll skip it because it’s optional, and the story details should be enough to mak | click |
| 8 | Create your book – StoryHearth | confused (-1) | I can see that something is loading, but there’s no explanation at all. I’m wondering whether it’s creating my book and whether I should wait, go back, or refresh. | wait_for_change |
| 9 | Your storybook – StoryHearth | confused (-1) | The book appeared, so the loading process did work, but it says “The Magical Adventrue of Sam” with a spelling error. It also says the illustration style is “Pop-art comic,” although I thought I selected “Watercolour.” I | flip_through |
| 10 | Your storybook – StoryHearth | frustrated (-2) | I’ve looked through every page, and the ending feels unfinished because it says Sam “would always remember” without telling me what she remembered. I’m also unhappy that the book is in pop-art comic style when I chose wa | click |
| 11 | Checkout – StoryHearth | suspicious (-1) | I found the price, but £45.97 feels higher than I expected because “Premium gift wrap” is already ticked without me asking for it. I want to see the actual cost without that add-on, so I’ll untick the gift wrap. I will n | click; read_page |
| 12 | Checkout – StoryHearth | suspicious (-1) | The price without the gift wrap is clearer now, but £37.98 is still more than I expected because shipping and handling adds £12.99. The countdown is making me feel rushed, and the page does not explain exactly when the r | done |
