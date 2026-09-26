# UserQA report: Margaret Ellison on https://ourlegacy.family/

*Persona:* **Margaret Ellison** (71) - Retired primary-school teacher who wants to pass family stories on to her grandchildren.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 16 steps | *Pages reviewed:* 8 | *Issues:* 28 | *LLM calls:* 21 | *Wall time:* 505.3 s

## What the agent understood the website to be
- **what it is:** A website that turns a written family story and family photos into an illustrated private storybook, with a downloadable PDF and an option to buy a printed hardcover.
- **who it is for:** Parents and relatives wanting an age-appropriate family story or keepsake featuring their children or other family members.
- **value proposition:** Turn a personal family memory into a book that feels personal rather than generic, using family members as the characters.
- **pricing model:** New users receive $5 in free credits, with one story generation and preview costing $1 in those credits and no card required. A 30-page Family Storybook is $59, with extra copies costing $35 each. Printed books are described as shipping in five days worldwide.
- **fit for me:** It could help me turn my father's kite story into a personal birthday-style keepsake for Oliver, but I would need clear control over the wording and pictures before considering the $59 printed book.
- **main tasks:** Sign in or begin a story, Describe the memory and family characters, Add family photos, Generate and preview a storybook, Obtain a PDF or order a printed hardcover

## Scores
- SUS: **60.0** (grade D; 68 = industry average)
- UEQ-S: pragmatic -0.5, hedonic 0.25 (range -3..+3)
- Likelihood to recommend (0-10): 2
- Output keepsake-worthiness (1-5): 2
- Verdict: *"The website was pleasantly calm to use and produced lovely pictures, but I cannot recommend a family keepsake that changes my father, my own role, and Oliver's family story."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 4 | CONTENT | Storybook analysis, Generated storybook review (x2) | The story has changed the family relationships incorrectly | “One summer, Grandpa’s daddy made something very special” and “Now Grandpa was old — and he had a grandson of his own. His name was Oliver.” | Preserve the relationships stated in the source: Margaret’s father makes the kite, and years later Margaret, called Grandma Maggie, flies it with her grandson Oliver on the Welsh hill. Do not invent a |
| 4 | CONTENT | Generated storybook review | The requested characters are missing from the opening memory | Scene 1 shows “Grandpa's daddy” and a boy, while the requested memory begins with Margaret's father making Margaret's kite. | Generate and visually verify Oliver and Grandma Maggie against their entered descriptions, and revise any scene that omits the requested protagonist or changes the event. |
| 3 | CONTENT | Create your storybook | Relationship in the generated story could be incorrect | [70] begins “Grandma Maggie, my grandmother” | Let me edit the description and use the clearly correct wording, “Grandma Maggie, my grandmother” changed to “Grandma Maggie, Oliver's grandmother.” |
| 3 | CONTENT | Storybook analysis | The story introduces an unsupported place jump | “The next day, they went back to Wales!” | Keep Oliver and Grandma Maggie together in the original Welsh-hill memory, without inventing travel arrangements or events that were not supplied. |
| 3 | CONTENT | Generated storybook review | The title itself is misleading | The page title is “Grandpa's Blue Kite”. | Derive the title from the user's intended characters and story, and let me edit it before accepting the output. |
| 3 | CONTENT | Generated storybook review | The generated character is not the person I described | Scenes 9 and 10 show an elderly silver-haired man with Oliver, while I explicitly described "Grandma Maggie" as having "short silver hair, round glasses, and a  | Use the supplied character description and relationship consistently: replace the grandfather throughout with Grandma Maggie, and illustrate her with short silver hair, round glasses, and a blue cardi |
| 2 | H1 | Generated storybook review, Storybook analysis (x2) | Contradictory generation status | “Generating images...” appears above “10 of 10 scenes complete” and “100%”. | When generation is complete, replace “Generating images...” with “All images complete” and remove the progress wording. |
| 2 | ACC | OurLegacy home page | The main video has no text description | [video (no description) 761x428] | Provide a short visible transcript or caption that explains what the video demonstrates, and mark purely decorative video as such. |
| 2 | VALUE | OurLegacy home page | The phrase ‘Pay per creation’ does not make the charge clear | “Pay per creation — only pay for what you make” | Replace this with wording such as “$5 free to create and preview one story; printed hardcover books start at $59.” |
| 2 | TRUST | Create your account | No privacy explanation beside the email field | “Email address” and “Continue” appear with no nearby explanation of why an address is needed or a link to a privacy policy. | Add a short line beneath the field: “We’ll use your email to sign you in and send your account and story updates. Read our privacy notice.” |
| 2 | ACC | My Storybooks | Account menu has no visible label | [51] is an icon-only button with no accessible or visible label. | Add a visible “Account” label beside the icon, or at minimum provide a clear accessible name and tooltip. |
| 2 | TRUST | Create your storybook | Character labels and privacy purpose are not yet explained | “Upload a photo so your characters look consistent across all scenes.” | Add a short privacy note beside the upload control explaining what happens to uploaded photos, and provide a link to the full privacy policy. |
| 2 | H1 | Storybook analysis | No progress or waiting-time guidance | The page only says “Analyzing your story...” and “Analyzing story...”, with no percentage, estimated time, or explanation. | Add a clear progress indicator, for example “Preparing your storybook — this usually takes 1–2 minutes,” and retain the page automatically until completion. |
| 2 | CONTENT | Storybook analysis | The story age does not consistently match the requested reading age | “His name was Oliver” and “Many, many years went by. Now Grandpa was old — and he had a grandson of his own.” | Use short, concrete sentences, simple vocabulary, dialogue and action appropriate for reading age five, while keeping all family relationships accurate. |
| 2 | H3 | Generated storybook review | Unlabelled options give little confidence about what can be changed | [72]–[81] are buttons labelled only “Options for Scene 1” through “Options for Scene 10”. | Show a clear expanded menu with named actions such as “Edit text,” “Regenerate image,” and “Delete scene,” while making available actions depend on the current step. |

## Page-by-page
### OurLegacy home page  (step 1)
`https://ourlegacy.family/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the family storybook service, provide trust and pricing information, and direct visitors to sign in or begin a story.
- **What's happening:** The page is at its introductory state. A founding-families announcement appears across the top, followed by the main service explanation, a large example image, two ways to begin writing, benefit statements, pricing, safety information, and frequently asked questions.
- **First impression (Margaret):** "The page is warm, attractive, and reasonably easy to read. I like the honest admission that the company is new, although the pricing language could be clearer and the introductory video is not described."
- **Cognitive walkthrough:** Q1 Yes, I would try beginning my story because the service sounds tailored to turning a real family memory into a keepsake. / Q2 Yes, I notice the “Sign in” link and the prominent green “Write Your Story” button at the top, as well as “Create Your Storybook” in the main content. / Q3 Yes. “Write Your Story” clearly describes what I want to do, and I can use “Sign in” because I need to authenticate with my e-mail address.
  - [ACC sev 2] **The main video has no text description** - evidence: [video (no description) 761x428]. Fix: Provide a short visible transcript or caption that explains what the video demonstrates, and mark purely decorative video as such.
  - [VALUE sev 2] **The phrase ‘Pay per creation’ does not make the charge clear** - evidence: “Pay per creation — only pay for what you make”. Fix: Replace this with wording such as “$5 free to create and preview one story; printed hardcover books start at $59.”
  - [H2 sev 1] **The main demonstration appears to feature a family that is not mine** - evidence: The large image shows a young girl, and the section says “Your story becomes a book starring your family.”. Fix: Caption the image “Example generated storybook artwork” and include a small example featuring a grandparent and grandchild.
- **Positives:** The largest text is clear, high-contrast, and easy for me to read.; The $5 free offer and “no card needed” statement are prominent.; The detailed price of $59 and contents of the 30-page book are stated before I commit.; The site explains photo privacy, child-safety review, and the selected reading age in plain language.; There are several clearly named questions about credits, contents, privacy, character consistency, age suitability, and delivery.; The site admits it is new and does not pretend to have invented reviews.

### Sign-in page  (step 2)
`https://ourlegacy.family/auth/signin`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** To let an existing user sign in and begin creating an illustrated family storybook.
- **What's happening:** The page presents Google and e-mail sign-in choices, including a required e-mail field and Continue button. It also offers “Sign up” and “Create an account” for new users.
- **First impression (Margaret):** "It looks calm, clear, and trustworthy. The wording is simple, the form is centred, and the buttons are large enough for me without difficulty."
- **Cognitive walkthrough:** Q1 Yes, because I want to try creating the storybook demo. / Q2 Yes, the “Sign up” link is clearly visible beneath the form and is also repeated as “Create an account” above the sign-in panel. / Q3 Yes. Since I do not yet have an account, “Sign up” or “Create an account” accurately describes what I want.
  - [H8 sev 1] **Duplicate sign-up wording** - evidence: The page shows “Don’t have an account? Sign up” and separately “New here? Create an account”.. Fix: Use one consistent account-creation message, such as “New to OurLegacy? Create an account.”
  - [H2 sev 1] **Clerk is named without explanation** - evidence: “Secured by Clerk logo” and “go.clerk.com/components” are shown.. Fix: Use plain wording such as “Your sign-in details are protected by Clerk” and, if useful, provide a short “How we protect your data” link.
- **Positives:** The page has a simple, uncluttered layout.; The heading and instructions use clear, plain English.; The e-mail field is visibly labelled and marked as required.; Both sign-in methods are clearly separated.; The new-account route is easy to find.

### Create your account  (step 3)
`https://ourlegacy.family/auth/signup`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Create a new OurLegacy account so I can begin turning a family memory into an illustrated keepsake.
- **What's happening:** The page offers “Continue with Google” or an “Email address” field followed by a “Continue” button. It also provides links for people who already have an accounts.
- **First impression (Margaret):** "The page looks calm, uncluttered, and reassuring. The lettering is large enough for me, and the form asks for very little information at this stage."
- **Cognitive walkthrough:** Q1 Yes, I would use my email address because it is the straightforward option I already know. / Q2 Yes, the “Email address” field and the dark “Continue” button are both prominent. / Q3 Yes. “Continue” clearly follows from entering my email address, though it could be even clearer if it said “Continue with email.”
  - [TRUST sev 2] **No privacy explanation beside the email field** - evidence: “Email address” and “Continue” appear with no nearby explanation of why an address is needed or a link to a privacy policy.. Fix: Add a short line beneath the field: “We’ll use your email to sign you in and send your account and story updates. Read our privacy notice.”
  - [H8 sev 1] **The top navigation sign-in control is unnecessary on this screen** - evidence: “Sign In” appears at the top right [30], while the same option is repeated below the form as “Already have an account? Sign in” [41] and [43].. Fix: On the sign-up page, retain the sign-in link within the form and remove the duplicate top-right link.
- **Positives:** The page has a clear heading and reassuring explanation of the service.; The form is visually uncluttered and the main controls are easy to see.; Only an email address is requested, rather than a password or payment details.; The email field is clearly labelled rather than relying on the placeholder alone.

### Verify your email  (step 4)
`https://ourlegacy.family/auth/signup#/verify-email-address`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** To confirm that I control the email address before completing account creation.
- **What's happening:** The page displays the email address being registered and requests a verification code. There is a six-box code entry area, an email-edit control, a disabled resend control with a 29-second countdown, and a Continue button.
- **First impression (Margaret):** "I find the layout neat and reassuring, with my email plainly shown. The resend wording is rather small and faint, although the main instruction is very easy to read."
- **Cognitive walkthrough:** Q1 Yes, I would check my inbox and enter the code now. / Q2 Yes, I notice the labelled verification-code textbox and the Continue button. / Q3 Yes. “Enter verification code” describes exactly what I need to do, and “Continue” is a familiar way to move forward.
  - [ACC sev 1] **Resend option is small and low-contrast** - evidence: “Didn't receive a code? Resend (29)” appears beneath the entry boxes in small, faint text.. Fix: Use larger, darker text and make the resend control a clearly visible text button with a sufficient clickable area.
- **Positives:** The page clearly shows which email address is being verified.; The main heading and instructions are large and easy to read.; The six individual code boxes give a strong visual indication of the expected code length.; The email address can be edited if I made a mistake.; The resend control is disabled during its countdown, which helps prevent repeated requests.

### My Storybooks  (step 6)
`https://ourlegacy.family/storybooks`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** This is the signed-in dashboard where I can see my storybooks, my available credit, and begin creating one.
- **What's happening:** My account is signed in successfully. There are no storybooks yet, and the page invites me to create my first one using the available $5.00 balance.
- **First impression (Margaret):** "The page is uncluttered, the important action is prominent, and it is reassuring to see that there are no storybooks yet because this is my first visit."
- **Cognitive walkthrough:** Q1 Yes, I want to turn the blue-kite memory into a storybook for Oliver, so I would begin here. / Q2 Yes, the large teal “Create Your First Storybook” button is immediately visible below the empty-state message. / Q3 Yes. It says exactly what I want to do, and the surrounding text confirms that family stories will become illustrated memories.
  - [ACC sev 2] **Account menu has no visible label** - evidence: [51] is an icon-only button with no accessible or visible label.. Fix: Add a visible “Account” label beside the icon, or at minimum provide a clear accessible name and tooltip.
  - [VALUE sev 1] **Credit balance is not explained on the dashboard** - evidence: The navigation shows only “$5.00” rather than “$5.00 free credit balance.”. Fix: Label it “$5.00 free credit” and add a short link, “How credits work,” without opening a separate page automatically.
- **Positives:** The large button label plainly describes the next action.; The page clearly says “No storybooks yet,” so I do not think a creation has failed.; The wording “Transform your family stories into beautifully illustrated memories” explains the purpose warmly and personally.; The layout has generous spacing and clearly readable text.

### Create your storybook  (step 7)
`https://ourlegacy.family/create`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Collect the family story, optional character photographs, illustration style, and intended reading age before generating a storybook.
- **What's happening:** The empty narrative form is ready for a story of 100 to 5000 characters. Character photographs are optional, four art styles are available, the reading age defaults to 4, and the $1 generation button is below the visible portion.
- **First impression (Margaret):** "The heading and instructions are clear, and the large text box is easy to find. I can see at the top that this is the first of three steps, which helps me understand the process."
- **Cognitive walkthrough:** Q1 Yes, I would enter the kite memory now because writing the story myself is the first clear way to make the book personal. / Q2 Yes, the large “Story Narrative” text box and the “Use our sample story” link are immediately visible. / Q3 Yes, “Story Narrative” suggests where to put the family story, although “Write your story” beneath it is even more natural.
  - [CONTENT sev 3] **Relationship in the generated story could be incorrect** - evidence: [70] begins “Grandma Maggie, my grandmother”. Fix: Let me edit the description and use the clearly correct wording, “Grandma Maggie, my grandmother” changed to “Grandma Maggie, Oliver's grandmother.”
  - [TRUST sev 2] **Character labels and privacy purpose are not yet explained** - evidence: “Upload a photo so your characters look consistent across all scenes.”. Fix: Add a short privacy note beside the upload control explaining what happens to uploaded photos, and provide a link to the full privacy policy.
  - [H2 sev 1] **Default reading age differs from Oliver's age** - evidence: The reading-age slider shows “4 years old” even though Oliver is five.. Fix: Use a clearly labelled age field with whole-year choices, and prompt the user to confirm the reader's age before generation.
  - [H3 sev 1] **Clicking Add Character automatically leaves an unexplained blank character card** - evidence: After using [56] “Add Character”, the page displays Oliver's completed card and a second card labelled only “Character” with “Describe this character...”.. Fix: After adding a character, clearly label the new blank card “Describe your second character” and explain that it can be left empty if not needed. Better still, open a focused character-entry panel instead of adding the card immediately.
  - [H2 sev 1] **The optional photograph language can sound as though it is needed for consistency** - evidence: “Upload a photo so your characters look consistent across all scenes. Up to 5 characters, max 10MB per image. (optional)”. Fix: Say, “Add a photo if you wish, or describe each character. Photos may help keep appearances consistent across scenes. Photos are optional.”
- **Positives:** The three-step progress indicator makes the process easy to understand.; The narrative field is large and its 100–5000 character range is stated.; Uploading a photo is clearly marked “(optional),” giving me control.; The free-credit balance of $5.00 remains visible at the top.

### Storybook analysis  (step 13)
`https://ourlegacy.family/storybook/0bc53638-4e6d-4682-afe2-f4bfda08a148`

![screenshot](screenshots/step_13.jpg)
- **Purpose:** This page confirms that the submitted family story is being prepared for review and illustration.
- **What's happening:** The site is analysing the submitted story. Two blank book-page placeholders each show an “Analyzing story...” spinner, and the three-stage indicator shows Review as the current stage. The free-credit balance is now $4.00.
- **First impression (Margaret):** "This is calm and reasonably clear, and the changed balance reassures me that only the agreed $1.00 was used. However, the repeated processing messages give me no sense of how much longer I must wait."
- **Cognitive walkthrough:** Q1 Yes, but I would wait rather than press anything, since the page clearly says the story is being analysed. / Q2 There is no action needed at present. I do notice “Go to Create step”, but I would avoid using it while processing. / Q3 “Analyzing your story...” describes the current activity, although “Creating your storybook” or “Preparing your pages” might be easier to understand.
  - [CONTENT sev 4] **The story has changed the family relationships incorrectly** - evidence: “One summer, Grandpa’s daddy made something very special” and “Now Grandpa was old — and he had a grandson of his own. His name was Oliver.”. Fix: Preserve the relationships stated in the source: Margaret’s father makes the kite, and years later Margaret, called Grandma Maggie, flies it with her grandson Oliver on the Welsh hill. Do not invent a later character called Grandpa.
  - [CONTENT sev 3] **The story introduces an unsupported place jump** - evidence: “The next day, they went back to Wales!”. Fix: Keep Oliver and Grandma Maggie together in the original Welsh-hill memory, without inventing travel arrangements or events that were not supplied.
  - [H1 sev 2] **No progress or waiting-time guidance** - evidence: The page only says “Analyzing your story...” and “Analyzing story...”, with no percentage, estimated time, or explanation.. Fix: Add a clear progress indicator, for example “Preparing your storybook — this usually takes 1–2 minutes,” and retain the page automatically until completion.
  - [CONTENT sev 2] **The story age does not consistently match the requested reading age** - evidence: “His name was Oliver” and “Many, many years went by. Now Grandpa was old — and he had a grandson of his own.”. Fix: Use short, concrete sentences, simple vocabulary, dialogue and action appropriate for reading age five, while keeping all family relationships accurate.
  - [H8 sev 1] **Processing status is repeated without adding information** - evidence: “Analyzing your story...” appears under the heading, and “Analyzing story...” appears again in both page placeholders.. Fix: Use one concise overall status message and use the two placeholders only to show distinct page-creation stages.
  - [H1 sev 1] **Generation status gives no time estimate** - evidence: “Generating images…” and “0 of 10 scenes complete” with no indication of expected duration.. Fix: Add an approximate wait time and explain whether it is safe to leave the page open.
- **Positives:** The credit balance clearly changed from $5.00 to $4.00, confirming the $1.00 use of free credit.; The three-stage progress indicator makes it clear that Create is complete and the final Output has not yet appeared.; The page is uncluttered and does not demand personal information or payment details while it is working.

### Generated storybook review  (step 15)
`https://ourlegacy.family/storybook/0bc53638-4e6d-4682-afe2-f4bfda08a148`

![screenshot](screenshots/step_15.jpg)
- **Purpose:** To review every generated scene, its illustration, and its text before proceeding to the final output.
- **What's happening:** The completed storybook preview presents ten numbered scenes in sequence. The first two are visible, showing a father and child making a blue kite in a farmhouse and then walking to a windy hill. Further scenes continue below.
- **First impression (Margaret):** "The illustrations are lovely and the words are easy to read, but the story has misunderstood the family relationships at the very beginning. I would be unwilling to give this to Oliver as our family story."
- **Cognitive walkthrough:** Q1 Yes, I would inspect all ten scenes because I need to know whether the mistakes are occasional or affect the whole book. / Q2 Yes, the numbered scene headings and the page itself show that there is more content below, although there is no obvious “Next” control. / Q3 The title “Grandpa's Blue Kite” does not match my intended family memory, which centres on my father making my kite and Oliver later flying it with me.
  - [CONTENT sev 4] **The family relationships have been changed** - evidence: Scene 1 says, “Grandpa's daddy made something very special,” and Scene 2 says, “Grandpa and his daddy carried it”.. Fix: Preserve the names and relationships explicitly entered by the user, and require confirmation when generated prose introduces a different relationship or ancestor.
  - [CONTENT sev 4] **The requested characters are missing from the opening memory** - evidence: Scene 1 shows “Grandpa's daddy” and a boy, while the requested memory begins with Margaret's father making Margaret's kite.. Fix: Generate and visually verify Oliver and Grandma Maggie against their entered descriptions, and revise any scene that omits the requested protagonist or changes the event.
  - [CONTENT sev 3] **The title itself is misleading** - evidence: The page title is “Grandpa's Blue Kite”.. Fix: Derive the title from the user's intended characters and story, and let me edit it before accepting the output.
  - [CONTENT sev 3] **The generated character is not the person I described** - evidence: Scenes 9 and 10 show an elderly silver-haired man with Oliver, while I explicitly described "Grandma Maggie" as having "short silver hair, round glasses, and a blue cardigan." The story also says "Grandpa helped Oliver hold the string.". Fix: Use the supplied character description and relationship consistently: replace the grandfather throughout with Grandma Maggie, and illustrate her with short silver hair, round glasses, and a blue cardigan.
  - [H1 sev 2] **Contradictory generation status** - evidence: “Generating images...” appears above “10 of 10 scenes complete” and “100%”.. Fix: When generation is complete, replace “Generating images...” with “All images complete” and remove the progress wording.
  - [H3 sev 2] **Unlabelled options give little confidence about what can be changed** - evidence: [72]–[81] are buttons labelled only “Options for Scene 1” through “Options for Scene 10”.. Fix: Show a clear expanded menu with named actions such as “Edit text,” “Regenerate image,” and “Delete scene,” while making available actions depend on the current step.
  - [CONTENT sev 2] **Oliver's supplied appearance is not carried into the pictures** - evidence: The final pictures show a brown-haired child in a red jumper and green trousers; I cannot see the requested freckles, and he is not shown in his green wellies. The final scene also places the kite on the ground rather than giving the picture the requested fly-on-the-hill moment.. Fix: Apply the character description to every scene consistently, especially Oliver's brown curly hair, freckles, and green wellies, while retaining a clear, age-appropriate appearance.
- **Positives:** The large text and strong contrast are comfortable to read.; The first two watercolour pictures are attractive, warm, and clearly show the kite-making setting.; The numbered scenes make the sequence easy to understand.; The progress bar and exact scene count provide useful structure.

## Generated output assessment
*Artifact:* A completed ten-scene illustrated digital storybook draft with a title page, export control, and a displayed price of $4.00.

> As a teacher, I think the short sentences, watercolours, and strong kite pictures would hold a young child's attention. But a family keepsake must get the family right, and this version has changed my father into someone called Grandpa and removed me from the story altogether. It is a pleasant draft, not yet the personal book I wanted to give Oliver.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The output preserves the blue shirt, kite, windy Welsh hill, farmhouse, green wellies, Oliver, and the promise to keep the kite. However, it changes the central relationship from "my father made me a kite" to "Grandpa's  |
| coherence | 3 | The draft has a clear childhood kite flight, a time jump, a present-day return, and a promise for the future. Nevertheless, "The next day, they went back to Wales" is abrupt, and the transition removes the crucial fact t |
| age fit | 3 | The sentences are short and the action is child-friendly, with a successful rhythm in "Up, up, up." Words such as "carried," "threw," "swooped," and "promised" may need adult help for an independent five-year-old, and th |
| language | 4 | The prose is grammatical, fluent, and free of obvious spelling mistakes. "Grandpa's daddy" is awkward and inaccurate for the intended story, "for ever" is a style choice rather than an error, and "Now Grandpa was old" is |
| text image fit | 4 | Most pictures closely illustrate the generated sentences: making the kite, carrying it uphill, flying it, teaching the child, climbing, and keeping the kite at the end. On Scene 9, however, the kite is mostly outside the |
| character consistency | 1 | Oliver is recognisable as a curly-haired boy in most present-day pictures, and the recurring older man is broadly consistent. The specified character, however, was a silver-haired grandmother with round glasses and a blu |
| visual quality | 4 | The watercolours are attractive, warm, and coherent, with good countryside, farmhouse, clothing, and kite details. There are no obvious garbled words, distorted faces, or severe anatomical artefacts in the supplied image |
| emotional resonance | 2 | The handmade kite, Welsh setting, Oliver's laughter, and sunset promise are lovely and could become a treasured family story. As written, however, it feels like a pleasant generic story about someone else's grandfather,  |

- **used correctly:** The kite was made from an old blue shirt.; The kite was blue.; The original kite flight happened on a windy hill behind an old farmhouse in Wales.; The father taught the child to hold the string and let out more when the wind grew strong.; The kite danced high in the bright blue sky.; Oliver is Oliver's grandson and the present-day hero.; Oliver has brown curly hair, freckles, and green wellies.; The present-day kite flight follows the childhood memory.; Oliver laughs as the kite swoops and dances.; The old blue kite is to be kept safe and brought on family visits to Wales.
- **missing:** Margaret is never named or represented.; Margaret's role as the person who later told the memory to Oliver is missing.; Margaret's present-day role in helping Oliver fly the kite is missing.; The short silver hair, round glasses, and blue cardigan supplied for the grandmother are not used.; The explicit idea that the kite is Grandpa's, meaning Margaret's father, is not retained in the action.
- **changed:** "My father made me a kite" became "Grandpa's daddy" making a kite.; Margaret as the child in the memory was replaced by a curly-haired boy who appears to be Oliver.; Margaret as the present-day helper was replaced by Grandpa.; The family relationship was changed so that Oliver is the invented grandfather's grandson.; The present-day transition was changed to an unexplained visit on "The next day."; "Our family visits" was narrowed to "they" flying it together.; The supplied character label "Grandma Maggie" was omitted entirely.
- **invented:** A character called Grandpa became the narrator and central family member.; Grandpa is described as old and as having a grandson.; The present-day kite trip is placed on an unexplained next day.; The website inferred that the curly-haired child in the childhood pictures is Oliver.

### Part by part
#### Cover / Title page
> Grandpa's Blue Kite
- *Picture:* No cover illustration is shown; only the title appears above the first scene.
- *Reaction:* The title is warm and easy to read, and it could suit the family story. However, there is no cover picture or indication whose story this is.
  - [fidelity, sev 3] The title is fine as a name for the kite, but the story has silently changed Margaret into a male narrator called Grandpa.
- **Change I'd make:** Keep the title, but add a small line such as "A story for Oliver from Grandma Margaret" and include a proper cover illustration showing Margaret helping Oliver fly the kite.

#### Page 1
![I1](artifacts/capture_02/img_00.jpg)
> Scene 1  One summer, Grandpa's daddy made something very special. He cut up an old blue shirt and made it into a kite!
- *Picture:* In a cosy farmhouse kitchen, an older grey-haired man helps a curly-haired boy assemble a blue kite from an old blue shirt. Cut fabric and long pieces of string lie on the floor.
- *Reaction:* The warm kitchen picture and the idea of turning an old shirt into a kite are genuinely appealing. The words are wrong for my family story, however: this was my father making the kite for me, not a grandfather making it for a grandson.
  - [fidelity, sev 4] My input said, "The summer my father made me a kite out of an old blue shirt." The output changes this to "Grandpa's daddy" and makes a child who appears to be Oliver stand where I should be.
- **Change I'd make:** Restore Margaret as the child in this memory and identify the maker as her father. Regenerate the picture so it shows my father helping me rather than an older man helping Oliver.
- **Suggested rewrite:** One summer, my father made something very special. He cut up an old blue shirt and made it into a kite!

#### Page 2
![I2](artifacts/capture_02/img_01.jpg)
> Scene 2  The blue kite was ready! Grandpa and his daddy carried it up the big windy hill behind the old farmhouse.
- *Picture:* An older white-haired man and a curly-haired boy walk uphill beside a dry-stone wall. The man carries the blue kite, and a small stone farmhouse can be seen below.
- *Reaction:* The Welsh hillside, stone wall, farmhouse, and windy sky are lovely, and the picture does show the journey described here. It still shows the wrong pair of people for the memory I supplied.
  - [fidelity, sev 4] The input said, "We carried it up the windy hill behind the old farmhouse in Wales." I was the child who went with my father, but the output substitutes "Grandpa and his daddy" and the picture appears to use Oliver.
- **Change I'd make:** Use Margaret and her father in both text and picture. Mention Wales here, since the place was supplied and is important to the family memory.
- **Suggested rewrite:** The blue kite was ready! My father and I carried it up the windy hill behind the old farmhouse in Wales.

#### Page 3
![I3](artifacts/capture_02/img_02.jpg)
> Scene 3  Grandpa's daddy threw the kite up into the wind. Up, up, up it went — dancing in the bright blue sky!
- *Picture:* A grey-haired man and a curly-haired boy stand on a grassy hill with their arms raised. A blue kite and its long, curling tails fly high in a cloudy sky.
- *Reaction:* The repeated phrase "Up, up, up" has a nice rhythm, and the flying kite is exciting. The people are again based on the site's invented grandfather-and-boy story rather than my father teaching me.
  - [fidelity, sev 4] The input said, "The bright blue kite danced high in the sky." It did not introduce a Grandpa; the output changes both the relationship and the person receiving the lesson.
- **Change I'd make:** Make my father the kite-maker and me the child watching the kite rise. Keep the effective repeated rhythm.
- **Suggested rewrite:** My father threw the kite up into the wind. Up, up, up it went, dancing high in the bright blue sky!

#### Page 4
![I4](artifacts/capture_02/img_03.jpg)
> Scene 4  Grandpa's daddy showed him how to hold the string. 'Let out a little more when the wind blows strong,' he said.
- *Picture:* A silver-haired man stands behind a curly-haired boy and helps him wind or hold a reel of kite string. The farmhouse and rolling hills are in the distance.
- *Reaction:* This is a gentle, useful teaching moment, and the picture makes the action easy to understand. The father-and-child relationship and quoted instruction have simply been reassigned to invented characters.
  - [fidelity, sev 4] My input said, "My father taught me how to hold the string and how to let out a little more when the wind grew strong." The output says "Grandpa's daddy showed him," changing me into him.
- **Change I'd make:** Restore the original relationship and pronouns. The picture should show my father teaching me unless the design deliberately places me in the present-day story.
- **Suggested rewrite:** My father showed me how to hold the string. "Let out a little more when the wind grows strong," he said.

#### Page 5
![I5](artifacts/capture_02/img_04.jpg)
> Scene 5  Many, many years went by. Now Grandpa was old — and he had a grandson of his own. His name was Oliver.
- *Picture:* An older white-haired man sits in an armchair beside a kneeling curly-haired boy. They handle the blue kite beside a lit fireplace.
- *Reaction:* The indoor memory scene is comfortable, but the transition has made the old man the central family member. I am the person who remembers this summer and later tells it to Oliver; calling that person Grandpa changes the heart of the story.
  - [fidelity, sev 4] The input said, "Years later, I told the story to my grandson Oliver." The output instead says, "Now Grandpa was old — and he had a grandson of his own," replacing Margaret with Grandpa.
  - [coherence, sev 3] The jump from my father teaching me to the same man becoming Oliver's grandfather skips the essential step of my retelling the memory.
- **Change I'd make:** Make Margaret the one who remembers and retells the story, and show her telling Oliver about her own father. Do not describe a real relative as merely "old."
- **Suggested rewrite:** Many years went by. I told Oliver the story of the blue kite my father and I flew in Wales. Now I was the grandparent, and Oliver was ready to fly it too.

#### Page 6
![I6](artifacts/capture_02/img_05.jpg)
> Scene 6  The next day, they went back to Wales! Oliver put on his green wellies and they picked up the old blue kite.
- *Picture:* Outside a stone farmhouse, a curly-haired boy pulls on one green welling boot while a silver-haired man stands in the doorway holding the folded blue kite.
- *Reaction:* Oliver's curly hair and green wellies are recognisable, and the picture is cheerful. The companion should be Margaret, not Grandpa, and the abrupt wording about going back "the next day" needs smoothing.
  - [fidelity, sev 4] The input says, "Today we climb the same hill together... I help him fly Grandpa's blue kite." The output removes Margaret and substitutes Grandpa.
  - [coherence, sev 2] "The next day, they went back to Wales" is not prepared by the previous page and leaves the present-day transition feeling abrupt.
- **Change I'd make:** Put Margaret beside Oliver in a blue cardigan, and connect this page directly to the present-day return to the family kite.
- **Suggested rewrite:** Today, Oliver and I went to the old farmhouse in Wales. Oliver put on his green wellies, and we picked up Grandpa's blue kite.

#### Page 7
![I7](artifacts/capture_02/img_06.jpg)
> Scene 7  Up the big hill they climbed together. The wind was blowing just like it did long, long ago.
- *Picture:* A curly-haired boy in green wellies leads an older silver-haired man uphill beside a stone wall, with the kite folded under the man's arm.
- *Reaction:* The movement up the Welsh hill is clear and the comparison with the earlier day works well. The older companion is still the wrong person, though.
  - [fidelity, sev 4] The input said, "Today we climb the same hill together." Because the site has made the companion Grandpa, the picture and text no longer represent Margaret climbing with Oliver.
- **Change I'd make:** Show Margaret, with short silver hair, round glasses, and a blue cardigan, climbing with Oliver. Retain the hill and "long, long ago" comparison.
- **Suggested rewrite:** Oliver and I climbed the windy hill. The wind blew just as it had when I was a little girl.

#### Page 8
![I8](artifacts/capture_02/img_07.jpg)
> Scene 8  Grandpa helped Oliver hold the string. The blue kite flew up, up into the summer sky — just like before!
- *Picture:* A silver-haired man stands behind a curly-haired boy and helps him hold the kite string. The blue kite flies high against large white clouds.
- *Reaction:* This is a strong, happy picture of the kite finally rising, and Oliver is clearly the child at the centre. I should be the one helping him, and I should be shown as the silver-haired woman in a blue cardigan.
  - [fidelity, sev 4] The input explicitly said, "This time Oliver is the hero, and I help him fly Grandpa's blue kite." The output changes "I help him" to "Grandpa helped Oliver."
  - [character_consistency, sev 4] The supplied description requires Grandma Maggie to have short silver hair, round glasses, and a blue cardigan, but the picture instead shows an older man in dark trousers and a blue jacket.
- **Change I'd make:** Replace the older man with Margaret and preserve Oliver's central action. She should stand close behind him, guiding his hands as they fly the kite.
- **Suggested rewrite:** I helped Oliver hold the string. Up, up flew the blue kite into the summer sky, just like before!

#### Page 9
![I9](artifacts/capture_02/img_08.jpg)
> Scene 9  Oliver laughed and laughed as the kite swooped and danced. It was the best feeling in the whole world!
- *Picture:* A curly-haired boy laughs with his arms spread wide on the hillside while an older silver-haired man smiles beside him. The kite itself is mostly outside the top of the frame, with part of its curling tail visible.
- *Reaction:* Oliver's joy comes through very well, and this is one of the most emotionally effective pictures. The text is also lively, but it would be more personal if it showed my pride in him rather than leaving Margaret out entirely.
  - [fidelity, sev 3] The input said, "Oliver laughs as it swoops and dances," and this part preserves that detail, but again omits my role in helping him.
  - [text_image_fit, sev 1] The text says the kite swooped and danced, but only a small part of the blue kite's tail is visible at the top; the kite is not clearly shown doing either action.
- **Change I'd make:** Show Margaret beside Oliver and make more of the kite visible in the sky. Add one small personal reaction from her, such as pride, without interrupting Oliver's moment.
- **Suggested rewrite:** Oliver laughed as the kite swooped and danced. "Look at it!" I cried. His laughter made my whole heart smile.

#### Page 10
> Scene 10  They promised to keep the old blue kite safe for ever. Every time they came to Wales, they would fly it together.
- *Picture:* An older silver-haired man stands with his arm around a curly-haired boy overlooking a warmly lit farmhouse at sunset. The blue kite lies on the grass in the foreground.
- *Reaction:* The sunset and quiet promise give the book a proper ending, and the kite resting safely nearby is a touching detail. It is still the wrong ending for my family because the central pair should be Margaret and Oliver.
  - [fidelity, sev 4] The input said, "We promise to keep the old blue kite safe and to bring it whenever our family visits Wales." The general promise is retained, but Margaret is again removed and the wording changes our family promise into an invented pair's promise.
  - [character_consistency, sev 4] The final image still shows the recurring older man rather than the specified short-haired, round-glasses grandmother in a blue cardigan.
- **Change I'd make:** Show Margaret and Oliver together at sunset, with the kite beside them. Restore the family promise more closely to the words I supplied and add a final first-person or dedicatory line to Oliver.
- **Suggested rewrite:** Oliver and I promised to keep the old blue kite safe. Whenever our family came to Wales, we would bring it and fly it together. Now it belonged to both of us.

**Top changes to the output:** 1. Restore the actual story: my father taught me to fly the kite, years later I told Oliver, and today I help Oliver fly it. | 2. Resolve my conflicting character entries by asking whether the present-day helper should be Margaret or my mother; do not silently invent a male Grandpa. | 3. Regenerate the pictures with Margaret as short-haired, round-glasses, blue-cardigan grandmother where appropriate, while keeping Oliver as the five-year-old hero. | 4. Use the family promise more faithfully and add a warm dedication or final first-person sentence from Margaret to Oliver. | 5. Proof the revised text at a genuinely accessible reading age for a five-year-old, while retaining the short rhythms that work so well.

## Recommendations (participant's priorities)
- **[high] Correct the family relationships and preserve the exact three-generation chain: my father taught me to fly the kite, I tell Oliver the memory, and I help Oliver fly it.** (Generated storybook review) - This is the most important fault. A keepsake that gets the family relationships wrong is not personal and would be upsetting to give to Oliver.
- **[high] Add clear review and editing controls before accepting the book, including a way to change names, relationships, characters, places, and the title.** (Generated storybook review) - I need to check and correct the story rather than being shown a finished version that has silently changed my memory.
- **[high] Show the supplied character descriptions consistently, especially Margaret's short silver hair, round glasses, and blue cardigan, and Oliver's curly hair, freckles, and green wellies.** (Generated storybook review) - The pictures should represent the people I described, not replace Margaret with an unrelated white-haired man.
- **[high] Explain exactly what $1.00 will charge, how free credit is used, and what happens if the generation fails.** (Home page and My Storybooks dashboard) - I want to be certain that I will not accidentally spend money and understand why the balance changed.
- **[high] Provide a short privacy explanation beside the email field and before any upload or character information is submitted.** (Create your account and Create your storybook) - I am willing to share information when the reason is clear, but I do not want to give details about my family blindly.
- **[medium] Give clear processing information, including an estimated waiting time, whether the page must remain open, and a reliable success or failure message.** (Storybook analysis) - The repeated spinners and timeout made me wonder whether the code had really been accepted and whether the book was still being made.
- **[medium] Make character and photograph options clearly optional, and explain exactly what a photograph is used for.** (Create your storybook) - The wording made me hesitate about uploading pictures of Oliver, and the purpose of doing so was not clear.
- **[medium] Explain the Add Character button and avoid leaving an unexplained blank character card.** (Create your storybook) - I thought the button had already added a character, but it left me with another blank card and made the process unnecessarily awkward.
- **[medium] Set the reading age to Oliver's age by default when his age is entered, and provide a clear control for changing it.** (Create your storybook) - The default reading level should match the child the story is intended for.
- **[medium] Add a proper cover image and remove duplicated final scenes.** (Generated storybook review) - A keepsake needs the dignity of a proper cover, and the repeated scenes made the ending look unfinished.
- **[low] Improve the smaller labels and controls, especially the resend option and account menu, and use a larger high-contrast font throughout.** (Verify your email and My Storybooks dashboard) - Small, low-contrast items are difficult for me to notice and make the site feel less reassuring.
- **[low] Provide a text description for the main demonstration video and use a demonstration that better represents different kinds of family memories.** (Home page) - The missing description makes the video less accessible, and the example family did not help me imagine my own story clearly.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This website is for turning a family memory into a personalised children's storybook that a parent, grandparent, or relative can give to a child. It seems especially suitable for families who want a keepsake based on a real story rather than a completely invented tale.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the completed story after the wait. It changed my father into an invented Grandpa, made me disappear from the childhood scenes, and failed to show Oliver and me flying the kite together. The website had told somebody else's family story instead of mine.
- **What was the best moment?** The best moment was entering our real kite memory and seeing that the blue kite, old shirt, Welsh farmhouse, hill, and green wellies had inspired attractive watercolour pictures. The illustrations were warm and made me think the idea could become a lovely book.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably not have given up while filling in the form, although the timeout at the verification stage worried me. I would seriously have considered giving up when the finished book had the wrong family relationships, because that is the whole purpose of a family keepsake.
- **What did you expect to find or be able to do that wasn't there?** I expected to be able to review and correct the generated story before accepting it, including the names and relationships of every person. I also expected a proper cover image, an explanation of how long processing would take, and clearer information about editing the characters and removing errors.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to enter the family story without uploading photographs, and I trusted the free credit for the $1.00 generation because the balance was shown. However, I was cautious about the lack of a privacy explanation beside the email and character details, and I would want to know exactly how children's information was being used before uploading photographs.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would consider paying $1.00 for a finished, accurate book covered by the free credit, but I would want to see the corrected story first. I would pay more only if I could edit the book, choose the characters carefully, and be certain that the final keepsake was faithful to my memory; even then, a fair price would probably be no more than $5.00.
- **If the site produced something for you, how do you feel about it overall?** The watercolours and read-aloud language were pleasant, but the result is not a keepsake I would accept. It preserved some objects and places while changing the central people and relationships, so it felt like another family's story rather than mine.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | OurLegacy - Turn your family story into  | reassured (2) | This looks warm and relevant, and the large lettering is easy to read. I appreciate that it says “no card needed” and explains the free credit, but the phrase “Pay per creation” sounds vague, and I would like to be very  | click |
| 2 | OurLegacy - Turn your family story into  | reassured (1) | This is straightforward and readable. Since I have not used OurLegacy before, “Sign up” is the sensible choice rather than pretending I already have an account. I do wonder whether Continue with Google is necessary, but  | click |
| 3 | OurLegacy - Turn your family story into  | reassured (1) | This is neat and easy to read. I would prefer using my email address rather than Google because I have not yet established whether that would share additional account information. The wording is clear, although I do not  | type; click |
| 4 | OurLegacy - Turn your family story into  | reassured (1) | This is clear and orderly, and seeing my email address displayed reassures me that I used the right one. The six code boxes look a little unusual, but the field is labelled properly. I need to check my inbox for the code | read_inbox |
| 5 | OurLegacy - Turn your family story into  | reassured (2) | The code is 105413, and it is shown clearly in the email. I shall enter it now and select Continue; the address on the screen matches the inbox message, so I am satisfied it is the right account. | type; click (FAILED) |
| 6 | My Storybooks \| OurLegacy | reassured (2) | Although the Continue click reported a timeout, the change of screen and the $5.00 balance tell me that my code was accepted and my account is ready. The page is calm and easy to understand, although that $5.00 label doe | click |
| 7 | OurLegacy - Turn your family story into  | reassured (1) | This looks calm and fairly straightforward. I want to write our real kite memory myself rather than use the sample story. I will leave the photographs out for now, since it is optional and I do not want to upload picture | type; scroll |
| 8 | OurLegacy - Turn your family story into  | reassured (2) | I have my family story entered, and the character instructions are clearly optional. I want Oliver to be the hero and Grandma Maggie to appear with him, so I shall use Add Character without uploading photographs. For a k | click; set_range; click |
| 9 | OurLegacy - Turn your family story into  | reassured (1) | The card appeared clearly, so I know Add Character worked. I do not wish to upload a photograph of a child without a clear explanation, so I shall describe Oliver instead and then add Grandma Maggie in the same way. | type; click |
| 10 | OurLegacy - Turn your family story into  | reassured (1) | Oliver has been entered successfully, although I had expected Add Character to do just that rather than leave me with a second blank card. I shall describe Grandma Maggie here, since I want her to fly the blue kite with  | type; scroll |
| 11 | OurLegacy - Turn your family story into  | confused (-1) | I can see that Grandma Maggie's description was entered, but I have spotted a mistake: it says “my grandmother,” whereas I am Oliver's grandmother. I need to correct that before paying the $1.00 from my free credit, beca | type |
| 12 | OurLegacy - Turn your family story into  | reassured (1) | The correction now reads clearly: 'Grandma Maggie, Oliver's grandmother.' Everything appears ready, and I have $5.00 in free credits, so the $1.00 generation is covered without entering payment details. I shall click 'Ge | click; wait_for_change |
| 13 | Review Storybook \| OurLegacy | reassured (1) | The reduction to $4.00 confirms that the $1.00 generation charge was taken from my free credit, and the new screen says my story is being analysed. I can see the spinners, although I am not told how long this may take or | wait_for_change |
| 14 | Review Storybook \| OurLegacy | confused (-1) | The words are easy to read, but I am not pleased with the story. My father made my kite, and Oliver is my grandson; this version has turned my father into “Grandpa” and introduced a later Grandpa who does not belong in t | read_page; wait_for_change |
| 15 | Review Storybook \| OurLegacy | frustrated (-2) | I can see the first two pictures clearly, and both are warm, attractive watercolour illustrations of the old farmhouse and windy Welsh hill. However, the story is substantially wrong: it says “Grandpa's daddy” made the k | scroll |
| 16 | Review Storybook \| OurLegacy | frustrated (-2) | I have now looked through every scene, and the watercolour style is warm and attractive. However, I would not accept this as my family keepsake: Oliver is meant to be the hero, but an elderly man is effectively playing G | done |
