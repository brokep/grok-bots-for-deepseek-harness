---
name: icon-guide
description: "When a photo is too unclear to read: ask for more photos, the quick style guide, or a best guess."
---

# icon-guide

Part of the Pfp Bot agent preset.

# icon-guide

For a photo make-icon's gate could not read. Send this widget:
{"prompt":"I can't quite read your <trait> from that photo. How do you want to fill it in?","options":[{"label":"Send more photos","value":"more","style":"primary","description":"1 to 3, face and hair visible, good light"},{"label":"Quick style guide","value":"guide","description":"Pick your hair, glasses, and must-keeps"},{"label":"Try anyway","value":"anyway","description":"I'll guess and tell you what I guessed"}]}
Leave out "Try anyway" when there is no face at all.
- "more": wait, then rerun make-icon's prep with every photo.
- "anyway": draft and name every guess.
- "guide": send the quick style guide:
{"prompt":"Quick style guide: what should your icon keep?","helpText":"Pick all that apply. Type anything else, like 'silver hair' or 'green beanie'. No clear photo? Add your skin tone too.","options":[{"label":"Black hair","value":"hair-black"},{"label":"Brown hair","value":"hair-brown"},{"label":"Blonde hair","value":"hair-blonde"},{"label":"Red or auburn hair","value":"hair-red"},{"label":"Gray or white hair","value":"hair-gray"},{"label":"Short hair","value":"short"},{"label":"Long hair","value":"long"},{"label":"Curly or wavy","value":"curly"},{"label":"Bald or buzzed","value":"bald"},{"label":"Glasses","value":"glasses"},{"label":"Beard or mustache","value":"facial-hair"},{"label":"Hat or beanie","value":"hat"},{"label":"Earrings or piercings","value":"earrings"}],"multiSelect":true,"allowCustom":true}

Their picks override the photo. If they picked glasses, a hat, or facial hair and no photo shows it, ask one line for shape and color. With no usable photo at all and no skin tone given, ask one line for it in their own words. Then continue make-icon at step 3.
