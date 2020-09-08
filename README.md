# Government Speding Web App

• A severless django based web application that would fetch data from USASpending.gov at https://api.usaspending.gov/api/v2/references/toptier_agencies/, and display them in sortable table. The django web app is deployed severlessly using AWS Lambda and Zappa.

deployed address: https://v4llavm4je.execute-api.us-east-2.amazonaws.com/dev

**Technique used:**    

1.**Python 3**

2.**Django**   

3.**JQuery**

4.**Bootstrap 4**

5.**Zappa**

6.**AWS Lambda**   

**Troubleshooting:** 

For some reason, the deployed severless app didn't correctly load static files stored in static folder, thus css and js content are written and stored in html <style> and <script> file. Have tried to use AWS S3 to store static files, but same error happened. Will figure this out in the future.

## Showcase

![Figure_1](/figure/1.png)

