
# Project Name

## Overview

### What is this website for?

one paragraph about what your website does

### What does it do?

one paragraph, or two describing what your website does

### How does it work

one paragraph describing how the4 website works
This website uses AngularJS to route viewers through the site and control which Javascript is executed. The site is styled with Bootstrap. The quiz has been created using Javascript and modal for enlarging images is displayed using some JQuery code. Bower has been used to manage package dependencies for deployment of site on github pages. The site can be viewed HERE

[Live Website]()

[GitHub Repository]()

## UX

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

### User Stories

- #### Things are slowly getting back to normal due to the pandemic, I want to plan my next holiday

1. I want to easily navigate the site relatively easily

2. I want to be able to see a balance of text, images and some video to get a glimpse of where I will be visiting

3. I want to be able to access links that direct me to important websites easily

4. I want some clicking interaction with the page so that I don't get bored

- #### As a previous who is using the website for reference

1. I want to have access to the website on any device and on the go

2. I want the navigation bar easily accessible so that I can get where I want quickly

### Design

#### Colour Scheme

Initially the colour scheme of the website was supposed to represent the national colours of the zimbabwean flag. However the colours were too bright and did not blend well together.

Instead, I used the idea that Zimbabwe has a lot of wild life, the colour was meant to mimic the savannah during a sunset. The colour is subtle without grabbing to much attention while giving more focus to the images. The main colour was picked using the colour picker on the header website to obtain the colour light salmon (#fdcba6) The buttons were matched using the compound approach from [adobe color wheel](https://color.adobe.com/create/color-wheel). to obtain the colour (#71C9A2)

<img src="./assets/images/readme-images/colour-scheme.png" height="100px"/>

#### Typography

- Font used for headings was Lobster with a back-up font of sans-serif. The font is eye catching and decorated white still easy to read.

<img src="./assets/images/readme-images/lobster-font.png" height="50px" />

- Font used for main text was Open Sans with a back-up font of sans-serif. The font is easy to read and well spaced out.

<img src="./assets/images/readme-images/open-sans-font.png" height="50px"/>

#### Imagery

- Images on the website were the top if not second priority on the website. They needed to supplement the text and offer visual aid to illustrate favourable tourist locations.

#### Mockups/wireframes

Mockups were made using Balsamiq Wireframes

[Mockup](./assets/planning/mockup-1.pdf)

- Wireframes were created using Adobe Xd, however, the layout and design was fallowed very loosely and changed during the mockup stage.
- [Mobile Wireframes](https://xd.adobe.com/view/9071beee-abcf-426e-6c19-ffe3212c5172-e640/) :point_left:

              <img src="./assets/images/readme-images/mobile-wire.png" />

  - [Desktop Wireframes](https://xd.adobe.com/view/d44aebce-000d-4a7c-4e4b-7ea4372b445b-a27b/) :point_left:

                    <img src="./assets/images/readme-images/desktop-wire.png" />

- #### Mockups

  - Mockups were also created using Adobe Xd and the final design of the webpage is very closely related hence I haven't included any screenshots.
  - [Mobile Wireframes](https://xd.adobe.com/view/97a16e82-02a0-41e3-598d-31bbba422cec-e190/) :point_left:
  - [Desktop Wireframes](https://xd.adobe.com/view/f42e5201-83f0-490e-75a5-c2ee85a8d6fb-821f/) :point_left:

### Existing Features

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

#### Common Features Across All Pages

- [x] **Header** - allows user to easily navigate across all pages

- Header is fixed to top of page for easy access (desktop and large tablets)
- Zimbabwe logo and text are positioned on the left and are links that take you to the homepage
- Navigation is place on the right on the logo for easy access (under logo for mobile)
- Navigation links change colour when hovered over. This lets the visitor know that it is clickable.
- Navigation link is underlined to let user know what page they are on
- Entire header disappears for mobile devices
- Colors have been chosen with optimum contrast in mind to be pleasant to the eye.
- [x] **Links** that are hovered over
- All links that are surrounding text have been underlined and change color when hovered over. This helps the user to identify external links. (except logo)
- [x] **Navigation banner**
- Navigation banner is the same across all pages to give uniformity and familiarity
- background image on home is scrollable to give a more fun user experience
- [x] **Accessibility**
- All images have aria labels in case they don't load and for the visually impaired
- [x] **Buttons**
- All buttons have the same styling and they invert colours when hovered (except for scroll to top button)
- [x] **Responsiveness**
- All pages work well with many screen sizes
- [x] **Footer**
- Footer sticks to the bottom of the page, regardless of the amount of content. This aids the overall user experience.
- All content have near uniform layout to give a nice and engaging flow of text and images
- Social links have been grouped together
- 'Contact us' is form for feedback and any question the user might have

### Specific to Pages

- [x] **Home Page**

- Image grid to easily see a handful of places the user can visit. When the mouse hovers you get addition information about the location

### Features Left to Implement

- Add a page where you can make a booking for a particular destinations. this includes adding a virtual online basket so that users can see what they have already selected (requires **Javascript** knowledge) For this reason I decided to remove the booking page from the website because it would be too incomplete and not provide a positive user experience.

- hide the scroll to top button at the beginning of page

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

### Languages used

- [**HTML**](https://en.wikipedia.org/wiki/HTML5)
- description of how it was used
- [**CSS**](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)

### Frameworks, Libraries and Programs Used

- [Fontawesome _v.5.15.3_](https://fontawesome.com/)
- We use **Font Awesome** javascript link to insert icons in the website to make site more visually appealing and easy to navigate.

- [Favicon](https://favicon.io/)
- Favicon.io was used to generate favicon and copied the syntax

- [Google Fonts](https://fonts.google.com/)
- Google Fonts was used to import 'Lobster' and 'Open Sans' fonts in the style.css stylesheet.

- [Visual Studio Code](https://code.visualstudio.com/)
- Source-code editor optimised fro debugging, syntax highlighting and extension support

- [Git](https://git-scm.com/)
- Git was used to allow for tracking of any changes in the code and for the version control.

- [Github](https://github.com/)
- GitHub is used to host the project files and publish the live website by using Git Pages.

- [TinyPNG](https://tinypng.com/)
- Used to reduce resolution of images

- [Bootstrap v4.5.0](https://getbootstrap.com/) - Used for the responsive layout as well as custom components such as image carousel, navigation bar, footer, cards, and collapse element.
- [jquery](https://jquery.com/) - Used in some of the clickable elements such as collapsible 'hamburger' nav bar and collapse element.
- [popper.js](https://popper.js.org/) - Used in some of the clickable elements such as collapsible 'hamburger' navbar and collapse element.
- [Font Awesome](https://fontawesome.com/) - Font Awesome was used to add social icons and complement the design.
- [Google Fonts](https://fonts.google.com/) - Google Fonts was used to import 'Exo' and 'PT Sarif' fonts in the main.css stylesheet.
- [Adobe Fonts](https://fonts.adobe.com/) - Adobe Fonts was used to import 'NeonStream' font which was the accent font in this project and cannot be found on Google Fonts website.
- [Git](https://git-scm.com/) - Git was used to allow for tracking of any changes in the code and for the version control.
- [GitPod](https://www.gitpod.io/) - GitPod, connected to GitHub, hosted the coding space and allowed the projected to be committed to the Github repository.
- [Github](https://github.com/) - GitHub is used to host the project files and publish the live website by using Git Pages.
- [Lightroom](https://www.adobe.com/ie/products/photoshop-lightroom.html?gclid=CjwKCAjwwYP2BRBGEiwAkoBpAqomS77OrQwQggC9QPnPACrkLBs-2AcrW9ZUvxbUJnFOgbRGKNeNEhoC95IQAvD_BwE&sdid=88X75SKS&mv=search&ef_id=CjwKCAjwwYP2BRBGEiwAkoBpAqomS77OrQwQggC9QPnPACrkLBs-2AcrW9ZUvxbUJnFOgbRGKNeNEhoC95IQAvD_BwE:G:s&s_kwcid=AL!3085!3!394412108599!e!!g!!lightroom) - Lightroom was used to edit and resize all images.
- [Photoshop](https://www.adobe.com/ie/products/photoshop.html?gclid=CjwKCAjwwYP2BRBGEiwAkoBpAuYIg7JHUAFtnRQB28LDaU5gvFxhLX_56PYV2xbl6bTKvYSjK5yoLhoCkjQQAvD_BwE&sdid=88X75SKS&mv=search&ef_id=CjwKCAjwwYP2BRBGEiwAkoBpAuYIg7JHUAFtnRQB28LDaU5gvFxhLX_56PYV2xbl6bTKvYSjK5yoLhoCkjQQAvD_BwE:G:s&s_kwcid=AL!3085!3!340674288378!e!!g!!photoshop) - Photoshop was used to create the background graphic for the Landing page as well as the favicon.
- [Adobe Xd](https://www.adobe.com/ie/products/xd.html) - Adobe Xd was used to create wireframes and mockups.
  - [UnDraw](https://xd.undraw.co/) - UnDraw plugin was used to obtain royalty-free graphics used in the 'Home' and 'Active' pages.
  - [ToolKit](https://manoharmanu.online/toolkit_plugin) - ToolKit plugin was used to obtain Royalty free images from UnSplash.
  - [Icons 4 Design](http://emsoftware.com/xdplugins/icons-4-design/) - Icons 4 Design was used to add some icons across the page such as the alert sign on the 'Informed' page.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:

- Go to the "Contact Us" page
- Try to submit the empty form and verify that an error message about the required fields appears
- Try to submit the form with an invalid email address and verify that a relevant error message appears
- Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

- ### Navigation bar

- When the logo or text is clicked, the user is redirected to the home page
- All links are working and have been tested.
- navigation bar is aligned vertically and under the logo for screens smaller than 660px
- The navigation bar stays at the top of the page for screens larger than 660px only

- ### Footer

- Footer always sticks to the bottom of the page and was tested by removing all content from the page.
- social media link open in a new tab when clicked
- When user accesses the 'Contact us' page

  - Name is required to continue submission
  - Email field is required and has to be in the correct format.
  - Text field has to contain at least two characters.
  - terms and conditions have to be ticked
  - When 'Submit' is clicked (given all fields have been filled out) the form will be sent

- ### The Image grid

- Any image that is hovered on (desktop only) the text is uniformly aligned and shows correct information for another device the grid is hidden and a continuous prose is displayed instead.

- ### External links

- All social links in the footer bring the user to the relevant social pages
- Links to external websites, the booking and visa button bring the user to the right website in a new tab.

- ### Internal Links

- Logo and text all lead to home page
- Navigation links lead to relevant pages
- Contact us link leads to the correct page for all web pages

### CSS3 validator

Pass

<a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border: 0; width: 88px; height: 31px;" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!" /></a>

### HTML5 Validator

**Home Page** - Pass
**About Page** - Pass
**Contact Us** - Pass
**Travel Information Page** - 2 Errors

1. Error: The element a must not appear as a descendant of the button element

From line 345, column 63; to line 345, column 118

`="button"><a href="https://www.evisa.gov.zw/home" target="_blank">Apply`

<!-- markdownlint-disable-next-line MD029 -->
2. Error: The element a must not appear as a descendant of the button element.

From line 376, column 38; to line 376, column 89

`="button"><a href="https://www.expedia.co.uk" target="_blank">Book f`

### Compatibility Testing

- Browser Compatibility

| Screen size\Browser |       Safari       |    Opera    | Microsoft Edge |       Chrome       |      Firefox       | Internet Explorer |
| ------------------- | :----------------: | :---------: | :------------: | :----------------: | :----------------: | :---------------: |
| Mobile              | :heavy_check_mark: | Not Tested  |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |
| Desktop             | :heavy_check_mark: | Not Tested. |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |
| Tablet              | :heavy_check_mark: | Not Tested. |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |

- OS Compatibility was tested on iOS 14.5.1, MacOS Catalina, iPadOS 14.5 It is yet to be tested on Unix, Linux, Windows or Solaris Operating Systems.
- The devices used in this testing include MacBook Pro, iPad Pro, iPhone 12 Pro Max, iPhone 7 Plus.

- The website was exhaustively tested for responsiveness on [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools). Different viewport sizes were simulated ranging from as small as iPhone 5 (320px) to large desktop sizes (1200px and above).

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

This website was published using [GitHub Pages](https://pages.github.com/).

1. Go to the GitHub.com and log in.
2. On the left-hand side, you'll see all your repositories, select the appropriate one.
3. Under the name of your chosen Repository you will see a ribbon of selections, click on 'Settings' located on the right hand side.
4. Scroll down till you see 'Pages' heading.
5. Under the 'Source' click on the dropdown and select 'master branch'
6. The page will reload and you'll see the link of your published page displayed under 'GitHub' pages.
7. It takes a few minutes for the site to be published, wait until the background of your link changes to a green color before trying to open it.

### Contribution

1. Firstly you will need to clone this repository by running the `git clone <https://github.com/datonex/visit-zimbabwe/>` command
2. If using VS Code type make sure you have th Git extension installed then type about code into your terminal
3. Download the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension, one installed find the go live button at the bottom right of your vscode window
4. The project will now run on [localhost](http://127.0.0.1:5500/)
5. If using Gitpod use the command `python3 -m http.server`
6. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits

### Content

Each bit of content must have its own link and displayed as a list

- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media

Each bit of content must have its own link and displayed as a list

#### Images

- video was obtained from [here](https://linkhere.com)

#### Audio

- audio was obtained from [here](https://linkhere.com)

#### Video

- video was obtained from [here](https://linkhere.com)

### Acknowledgements

I received inspiration for this project from following tourists sites

- Thank you to my mentor for his support and guidance
