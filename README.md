# Wellcome to the insta scrapper! This application can get information about public users accounts. IT WAS USED ONLY FOR EDUCATION PURPOSE! ALL RIGHT ARE RESERVED!

## To use this app you have to have python v3.6 (i used it.) and Google Chrome v107 

## Best practice is creating virtual env and using it.

```bash
    python -m venv <env-name>
    ./<env-name>/Scripts/activate
```

## Next to use libraries you should install dependencies

```bash
    python -m pip install -r requirements.txt
```

## When dependencies are installed you can run the server

```bash
    python server.py
```

## Short documentation

url-to-scrap\* - url to scrap, replace it with url from instanavigation website

-   example: https://instanavigation.com/ru/profile/instasamka
-   where: "instasamka" = < profile-name >
    wich you can replace with any public username

```bash
    http://127.0.0.1:5000/?url=<url-to-scrap>
```

-   example of using:

```bash
    http://127.0.0.1:5000/?url=https://instanavigation.com/ru/profile/instasamka
```

will give the following JSON.

```json
{
    "biography": "INSTASAMKA $$$$$$",
    "main_image": "https://cdn.instanavigation.com/?https://scontent-dus1-1.cdninstagram.com/v/t51.2885-19/310188153_185336297361246_1190635051221148933_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-dus1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=qvaO1l0JCHYAX_uljfI&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDSkDr9sPFXEkcnGoImsXr1Z0_kltCLAq_EZ9zsdGsuaQ&oe=63788F5E&_nc_sid=8fd12b",
    "main_info": {
        "publications_count": "219",
        "subscribed_count": "235",
        "subscribers_count": "5,433,831"
    },
    "nickname": "instasamka",
    "posts": [
        {
            "date": "15 November 2022 09:29:14",
            "description": "🌷",
            "image": "https://cdn.instanavigation.com/?https://scontent-dus1-1.cdninstagram.com/v/t51.2885-15/315575171_488204679952120_4365689642776739600_n.jpg?stp=c0.180.1440.1440a_dst-jpg_e35_s640x640_sh0.08&_nc_ht=scontent-dus1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=KZGGJShbrUIAX9tUkhP&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDRDVGObiSUTD0idfHOTW2vRCCKNrm-sq0F60HHK6-SRA&oe=63780060&_nc_sid=8fd12b"
        },
        {
            "date": "10 November 2022 09:36:08",
            "description": "🔮🧿🪬🕍🤍",
            "image": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
        },
        {
            "date": "07 November 2022 10:38:16",
            "description": "🔗🪩🤍🎧\n\nph: @marvil_dancee",
            "image": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
        }
    ],
    "profile_name": "\n                    PR Director: @mstolyarov💵\n(maxim@namnecash.ru)\n🪐☄️\nKAZAKHSTAN 🇰🇿 TOUR 🪩 TICKETS:\n                "
}
```
