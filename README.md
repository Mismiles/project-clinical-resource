## Clinical resource tool

The project aims to provide a search engine for professionals to look for resources related to their role. 
The current method of finding resources and guidlines involves clicking through folders to find files.
Often these files are dublicated and also hard to differentiate for different professionals.
The aim is to build a search engine for users to look for guidance and also be able to create, 
read, update and delete attchments and resources as necessary. 
 
## UX

The website has six main target audiences. Doctors, nurses, pharmacists, physiotherapists, occupational
therapists and pharmacy technicians. Traditionally, information is stored in files and often one professional
will ask another of a way to find that file. Not only is this process time consuming, but often multiple resources
will have the same name, but will only be relevant to a specific profession. It is therefore not only difficult to
find such resources, but even when they are found, it is hard to know if is relevant to the individual.

The project aims to reduce error, improve accuracy of searching for resources and allow users to imput data to build
a more effective search system.

...........

...........



## Wireframe

Click to see the wireframe link for desktop browsers. The mobile version does not contain the PDF document to minimise
screen switching.

https://drive.google.com/file/d/1fpjlTmFjG2F_fiG67_HgJ0i6IJcptLUw/view?usp=sharing

## Features

Once loading the page, a disclaimer appears. This is to ensure that the user cannot use the tool to calculate doses 
for patients outside of this criteria.

If the user wishes to view the hospital guideline (on desktop only), they can have it adjacent to the form by clicking 
"click to display guideline on right of page."

The guideline is fixed as the user goes through the tool to allow them to refer to it at any time. 
This is done without either side of the webpage interfering with the user experience.

The user can then click "none of the above apply (click to use tool)" as a safety button which then brings up the tool.

The indication is placed to force the user to specify why vancomycin is being used.

The "on renal replacement therapy?" question is placed to specify if the patient is on dialysis.

The patient's gender, age, weight, the date their weight was taken, their
height and serum creatinine will need to be entered in order to allow the tool to calculate the patient's renal
function, the correct dose and how often to monitor the patient.

There is a 30 day limit on the calendar to prompt the user to obtain a recent weight.

The "I confirm that this tool takes no clinical responsibility for outcomes and I will use this tool only 
to aid my ultimate clinical decision" button is placed to prompt the user that ultimately the prescribing decision is theirs
and that this tool will only aid that decision.

The "click to display dose and monitoring advice" takes into account all inputted factors to give a dose. It does this
by calculating the patient's body mass index (BMI), ideal body weight, their renal function (CrCl) and uses their weight 
to advise on the initial (STAT) dose.

The next feature "click to show dosing rationale" explains to the user why the outputs were generated and also shows 
(by highlighting dosing and monitoring tables) where the dosing and monitoring advice is obtained from. 

To ensure scrolling is minimised, a function to scroll has been added when clicking the disclaimer, 
calculate dose button and show dosing rationale button.


### Existing Features
The first feature (the guideline) allows the user to reference the guideline for prescribing advice.

The next feature (the form) prompts the user to collect all data required to process the form safely and effectively.

The calendar has a safety limit of 30 days to prompt the user to input a recent weight so that an old weight is not used.

The dosing advice section then takes all the information and displays the appropriate dose and monitoring to undertake.

The explain rationale section then breaks down why the dose and monitoring advice was chosen.

### Features Left to Implement
Another feature idea for the future could be to obtain all the input values and email them to an email address. This could then
be used to audit prescribing.

Additionally, this could be used to prompt a pharmacist who has access to this email to contact colleagues looking after the patient
that they have a patient who is on vancomycin.

A form validation function can be added to prompt the user to fill in fields that have been missed.


## Technologies Used

The technologies used include:

- [Html]
The basis of the project was made using HTML

- [CSS]
CSS was used to add styles on top of Bootstrap

- [Bootstrap] (https://getbootstrap.com/)
Bootstrap was used for styling, the form and formatting positioning.

- [Vanilla Javascript] 
This project uses javascript to add functionally. Additionally it uses Javascript to calculate 
ideal body weight, body mass index, creatinine clearance (kidney function), the initial dose of vancomycin, 
the maintenance dose of vancomycin and the frequency of monitoring of the drug.

- [JQuery](https://jquery.com)
The project uses **JQuery** to simplify DOM manipulation. In this project, it was only used for the bootstrap features.

## Testing

The code was tested using jshint.com. No major issues were identified.

The tool was tested on both mobile and desktop screens.

As the aim is for the tool to be implemented in a clinical setting and for screen switching to be minimised as much as possible.

The the webpage has been tested on windows desktops. Note that it was not tested on 4k resolutions as these were not present
in the hospital computers.

The webpage was tested on chrome, internet explorer and firefox.

The webpage was also tested on the following mobile devices:
Huawei Mate 20 pro
iPhone 7
Samsung Galaxy s8
Samsung Galaxy S10

1. Testing the tool:
    1. Click the disclaimer
    2. Fill in all the fields
    3. Submit the form and compare the results to the guideline
    4. Click "click to show dosing rationale" to identify how the recommendations were calculated.


Note that the guideline is intentionally hidden on mobile devices. This is to minimise screen switching.

The calendar does not appear on internet explorer.

## Deployment

To run the project, simply go to https://mismiles.github.io/project-clinical-calculator/

## Credits

### Content
- The top clickable arrow to show the guideline was adapted from http://code-chunk.com/chunks/543df4c394758/bootstrap-arrow-shaped-buttons
- The code for the calendar was obtianed from https://stackoverflow.com/questions/32378590/set-date-input-fields-max-date-to-today 
. This was then adapted to display the minimum date (30 days prior).
- The scrollby function was obtained from https://www.w3schools.com/jsref/met_win_scrollby.asp and then adapted.

### Media
- PDF from this document was taken from a local hospital guideline, obtained from the Whittington health
intranet page

### Acknowledgements
- My colleague and consultant antimicrobial pharmacist Ai-Nee Lim who was pivotal in the design of
the vancomycin antimicrobial guideline.
- My colleague Dr Nitzan Lindenberg who took his time to aid in the initiation step of building this tool
and providing constructive feedback throughout.
- My colleagues Anja Ritchter, Chandini Kanderia, Dr Howell Jones, Ian Man and Patricia McCormick for testing the tool.
