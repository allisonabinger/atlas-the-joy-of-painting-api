  <h1 align="center">
  <img src="./assets/bob-ross-banner.jpeg" align="center">
   The Joy of Coding</h1>
  <h3 align="center">Exploring ETL with Bob Ross!</h2>


# Introduction

This project was designed to explore the concept of **ETL (Extract, Transform, Load)**, which is the process of taking data from multiple unique sources, modifying or *cleaning* the data to be more uniform, and storing them in a centralized database.

[The Joy of Painting](https://en.wikipedia.org/wiki/The_Joy_of_Painting) is a television show that ran from 1983 until 1994, and featured the ever-so-tranquil [Bob Ross](https://en.wikipedia.org/wiki/Bob_Ross) instucting the public on the painting techniques, life lessons, and the beauty of nature. This project started with a hypothetical news station who had gathered data on the paintings and episodes of the show, but needed a better way for their viewers to search and query different details about the content. Starting with CSV and TXT files, **The Joy of Coding** contains a program to query and organize the large amount of data for easier access to viewers. 

# Data Structure

Each entry in the database is unique to the painting that was made. It contains attribtues for the user to search and organize by:
```

Each Painting has the following:
    ID: Unique for the painting
    TITLE: The Title of the painting
    AIR_DATE: The date the episode featuring the painting aired
    SPECIAL_GUEST: A name of a special guest on the episode, or None if not
    EPISODE: Season/Episode number in the S##E## format
    SUBJECTS: Objects or subjects of the painting featured (e.g. bushes, trees)
    IMAGE_URL: Contains an image of the painting
    VIDEO_URL: A link to a YouTube video of the episode
    NUM_COLORS: The total number of paint colors used in the painting
    COLORS: An array of the colors used in the painting, including the name and hex code value
```


# Usage

This program does not feature a fully functional front-end at this time, but progress is being made. At this point, the sorting can be done by accessing the API with curl requests.

### Start the Server
In a terminal, navigate to the `server` directory, and run `npm run start-server`. The system will display two messages to verify your server status and connection to the paintings database.

```
$ npm run start-server
> files_manager@1.0.0 start-server
> NODE_NO_WARNINGS=1 nodemon --exec babel-node --presets @babel/preset-env ./server.js

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env ./server.js`
Server is running on port 5000
Connected to MongoDB Atlas


```
### Query the API
In another terminal, use `curl` (or access using your browser with 0.0.0.0:5000/paintings) to query the API. 

There is only one endpoint, `paintings/`, which without any parameters will give you all 403 paintings in the database.

The projection for each painting will be the Title, Air Date, and Episode Number. This will be adjusted for the front-end.


### Sort by Month (Air Date of the Painting)

The API will accept the `months` parameter to query based on the month that the episode aired. The month will need to be in the numerical format (01 for January, 02 for February), or using the accepted abbreviation format (mar for March, apr for April). The query parameter must be `months` regardless if a single month or multiple months are queried.

```
curl 0.0.0.0:5000/paintings?months=jan
[
  {
    "title": "A Walk in the Woods",
    "air_date": "01/11/83",
    "episode": "S01E01"
  },
  {
    "title": "Mount McKinley",
    "air_date": "01/11/83",
    "episode": "S01E02"
  },
...
]
```

### Sort by Color

The API will accept the `colors` parameter to query based on the colors used in the painting. The format for the color requires a `+` symbol for any spaces. The query parameter must be `colors` regardless if a single color or multiple colors are queried.

The following colors are available to query with, please note that these are the original color names and not chosen by the programmer:
- Black Gesso
- Bright Red
- Burnt Umber
- Cadmium Yellow
- Dark Sienna
- Indian Red
- Indian Yellow
- Liquid Black
- Liquid Clear
- Midnight Black
- Phthalo Blue
- Phthalo Green
- Prussian Blue
- Sap Green
- Titanium White
- Van_Dyke Brown
- Yellow Ochre
- Alizarin Crimson


```
$ curl 0.0.0.0:5000/paintings?colors=Titanium+White
[
  {
    "title": "Quiet Stream",
    "air_date": "02/01/83",
    "episode": "S01E05"
  },
  {
    "title": "Winter Moon",
    "air_date": "02/08/83",
    "episode": "S01E06"
  },
  {
    "title": "Autumn Mountains",
    "air_date": "02/15/83",
    "episode": "S01E07"
  },
  ...
]
```

### Sort by Subject Matter

The API will accept the `subjects` parameter to find specific items or subjects painted by Bob. The following subjects are available to query with, replacing the space between words with a `+` is necessary for quering:

|                    |                    |                   |                 |
|--------------------|--------------------|-------------------|-----------------|
| Apple Frame        | Aurora Borealis    | Barn              | Beach           |
| Boat               | Bridge             | Building          | Bushes          |
| Cabin              | Cactus             | Circle Frame      | Cirrus          |
| Cliff              | Clouds             | Conifer           | Cumulus         |
| Deciduous          | Diane Andre        | Dock              | Double Oval Frame|
| Farm               | Fence              | Fire              | Florida Frame   |
| Flowers            | Fog                | Framed            | Grass           |
| Guest              | Half Circle Frame  | Half Oval Frame   | Hills           |
| Lake               | Lakes              | Lighthouse        | Mill            |
| Moon               | Mountain           | Mountains         | Night           |
| Ocean              | Oval Frame         | Palm Trees        | Path            |
| Person             | Portrait           | Rectangle 3D Frame| Rectangular Frame|
| River              | Rocks              | Seashell Frame    | Snow            |
| Snowy Mountain     | Split Frame        | Steve Ross        | Structure       |
| Sun                | Tomb Frame         | Tree              | Trees           |
| Triple Frame       | Waterfall          | Waves             | Windmill        |
| Window Frame       | Winter             | Wood Framed       |                 |


Here is an example of querying with the subject matter:

```
$ curl 0.0.0.0:5000/paintings?subjects=River
[
  {
    "title": "Quiet Stream",
    "air_date": "02/01/83",
    "episode": "S01E05"
  },
  {
    "title": "Lazy River",
    "air_date": "11/02/83",
    "episode": "S02E10"
  },
  {
    "title": "Black Waterfall",
    "air_date": "11/09/83",
    "episode": "S02E11"
  },
  {
    "title": "Bubbling Stream",
    "air_date": "01/18/84",
    "episode": "S03E03"
  },
...
]
```

### Querying with Multiple Filters

Parameters can be combined using the `&` symbol between them. Here is an exmaple of a very specific search:

```
$ curl 0.0.0.0:5000/paintings?months=may&colors=Titanium+White&subjects=tree
[
  {
    "title": "Blue River",
    "air_date": "05/01/85",
    "episode": "S06E01"
  },
  {
    "title": "Nature's Edge",
    "air_date": "05/08/85",
    "episode": "S06E02"
  },
...
]
```

#### Please let me know of any additional features or bugs that should be brought to my attention!

---
This README was made with :heart: by Allison Binger, student at Atlas School Tulsa. Find me on [GitHub](https://github.com/allisonabinger) or [LinkedIn](https://linkedin.com/in/allisonbinger)! :smile_cat:







