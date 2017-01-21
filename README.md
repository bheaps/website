Welcome to ExploringIceAxe; a website for hikers and mountaineers. There are three parts to this site, trip reports, trails/routes, and pictures of the day. A trip report is a story of a hiking/mountaineering trip; a trail/route is a description of how to get (drive) to the start of the trail, and instructions for reaching the objective be it a mountain top, viewpoint, whatever; and picture of the day is a place to share your favorite hiking/mountaineering related photos. This is not a completed website, but complete enough to showcase my skills.

I decided to make this website with django; a python web library along with a mysql database. Django is very useful for extracting data from databases and displaying it on an html page, and saving data from html forms to a database. I did not use any form code from wordpress or the like, I wrote all the html and python myself using various open source libraries; haystack for searching, ckeditor for richtext html forms, and boostrap for styling. ExploringIceAxe is accessible at http://bheaps.pythonanywhere.com (hosted for free with pythonanywhere).

OK the main page, a hiking image carousel on the left, on the right the five most recent "trip report" additions; trip reports will be the most likely reasons for a visit to this website. And below the image carousel Search Reports and Search Trails if a visitor comes to the site with a specific title in mind. Go ahead and try searching for "Alcoholic". The search results page gives the user the option to try trails and reports or switch to the other.

To contribute a report or a trail/route to the website you need to register and log in. Click on Register in the top right, fill out the fields (dont forget your username and password) and click Register. Now click Login in the top right, login with your username and password. Obvious future improvement will be email confirmation for registration. Now choose "Post Trip Report" on the navigation bar. Fill in a title "SAP test" and "SAP lorem ipsum" in the main text box; then click the Add Report button at the bottom of the page. Now click the Home button on the navigation bar and you will see your report at the top of the list. Obvious future improvement would be having an admin inspect before a report is published. Don't worry about adding bad data to the website, you are the only person other then myself looking at this website, and once you have added some data I will know you have looked at the website. If you open your trip report notice that there is a modify link, a user can modify any report they submit. Now click the Trip Reports button on the navigation bar and have a look at the Alcoholic Traverse, it is a great read and the intended type of content for this website. Notice how at the bottom of the page a user and like/dislike and comment on a report. In the future when there are a lot of reports on the site the pagination will be more appreciated.

Trails works very similarly to reports, you just need to add more information as hikers will tend to sort their options by time, trail distance and elevation gain. To add a trail/route click on Add Trail/Route on the navigation bar. Feel free to add a trail if you want, just fill in the data fields and then you can locate your trail sorted alphabetically on the Trails/Routes page. Users can like/dislike and comment on a trail/route; and users can modify trails/routes they submitted.

Click on Picture of the day on the navigation bar; as you can see at the top left below the navigation bar you can sort by number of likes/dislikes or by the date the photo was submitted. It is very simple to add a picture, feel free to add one if you like.

If you would like to look at my code, it is all on github at https://github.com/bheaps/website . I doubt you would be interested in looking at it all, I will recommend looking at https://github.com/bheaps/website/blob/master/reports/views.py , the function detail on line 38 handles the viewing of a trip report (ex. Alcoholic Traverse) then look at the html template https://github.com/bheaps/website/blob/master/reports/templates/reports/details.html and look for the {{ }} elements that get filled in with database values. Also interesting is the create function on line 66 of https://github.com/bheaps/website/blob/master/reports/views.py and the corresponding template https://github.com/bheaps/website/blob/master/reports/templates/reports/create.html . All html pages reference https://github.com/bheaps/website/blob/master/reports/templates/base.html with django html code, the extends function. Feel free to look around.

If you have any questions or comments please email me at bheaps99@gmail.com

Thank you for taking the time to read about my website. I am looking forward to hearing from you.
