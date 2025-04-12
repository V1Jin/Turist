import sqlite3
import json
import base64

path = "D:/Programming/Turism/backend/"
with open(path + "audio/1.txt", "rb") as file:
    file.close()

    

baseDir = 'D:/Programming/Turism/backend/audio/'
data = [
    {
      "name": "Олимпийский парк",
      "coordinates": [39.9602, 43.4022],
      "info": "Комплекс спортивных сооружений, построенный для зимней Олимпиады 2014 года. Включает ледовые арены, стадион 'Фишт' и олимпийскую площадь."
    },
    {
      "name": "Роза Хутор",
      "coordinates": [40.2556, 43.6756],
      "info": "Популярный горнолыжный курорт в Красной Поляне. Зимой — катание, летом — треккинг и канатные дороги."
    },
    {
      "name": "Морской вокзал",
      "coordinates": [39.7204, 43.5855],
      "info": "Архитектурный символ Сочи с башней и шпилем. Отсюда отправляются прогулочные катера и яхты."
    },
    {
      "name": "Парк Ривьера",
      "coordinates": [39.7198, 43.5911],
      "info": "Один из старейших парков города с аллеями, аттракционами и дельфинарием. Отличное место для семейного отдыха."
    },
    {
      "name": "Скайпарк",
      "coordinates": [39.9111, 43.5944],
      "info": "Экстремальный парк развлечений с самым длинным подвесным мостом в России и возможностью прыжков с высоты."
    },
    {
      "name": "Сочи Автодром",
      "coordinates": [39.9575, 43.4038],
      "info": "Современная трасса для Формулы-1, расположенная в Олимпийском парке. Проводились Гран-при России."
    },
    {
      "name": "Дендрарий",
      "coordinates": [39.7342, 43.5709],
      "info": "Ботанический сад с коллекцией растений со всего мира, пальмами, фонтанами и канатной дорогой."
    },
    {
      "name": "Сочи Парк",
      "coordinates": [39.9583, 43.3983],
      "info": "Первый тематический парк в России, вдохновлённый русскими сказками и героями. Развлечения для детей и взрослых."
    },
    {
      "name": "Красная Поляна",
      "coordinates": [40.2106, 43.6761],
      "info": "Курортный посёлок в горах, место активного отдыха и лыжного спорта. Один из центров зимней Олимпиады."
    },
    {
      "name": "Агурские водопады",
      "coordinates": [39.8475, 43.5556],
      "info": "Живописные водопады в Агурском ущелье недалеко от горы Ахун. Популярное место для пеших прогулок."
    },
    {
      "name": "Краснодарский стадион",
      "coordinates": [39.0181, 45.0355],
      "info": "Современный футбольный стадион, построенный по инициативе Сергея Галицкого. Известен уникальной круглой архитектурой и парком рядом."
    },
    {
      "name": "Парк Галицкого",
      "coordinates": [39.0175, 45.0343],
      "info": "Один из самых красивых городских парков России. Современный ландшафтный дизайн, фонтаны, амфитеатр, зоны отдыха и искусственные холмы."
    },
    {
      "name": "Краснодарская филармония",
      "coordinates": [38.9794, 45.0301],
      "info": "Историческое здание и центр музыкальной культуры. Здесь проходят концерты классической и современной музыки."
    },
    {
      "name": "Кубанский казачий хор",
      "coordinates": [38.9887, 45.0332],
      "info": "Один из старейших и известнейших народных коллективов России. Располагается в здании с музеем и концертным залом."
    },
    {
      "name": "Центральный парк имени Горького",
      "coordinates": [38.9840, 45.0274],
      "info": "Исторический парк в центре города с аллеями, аттракционами, прудом и сценой для концертов. Любимое место прогулок горожан."
    },
    {
      "name": "Улица Красная",
      "coordinates": [38.9765, 45.0284],
      "info": "Главная улица Краснодара. По выходным становится пешеходной. Здесь проходят парады, фестивали и гуляния."
    },
    {
      "name": "Свято-Екатерининский кафедральный собор",
      "coordinates": [38.9799, 45.0339],
      "info": "Главный православный храм города, построенный в неовизантийском стиле. Назван в честь святой Екатерины."
    },
    {
      "name": "Чистяковская роща",
      "coordinates": [39.0001, 45.0500],
      "info": "Зелёная зона в центре города с вековыми деревьями, детскими площадками, мини-зоопарком и прогулочными дорожками."
    },
    {
      "name": "Смотровая башня на улице Захарова",
      "coordinates": [39.0148, 45.0351],
      "info": "Необычное место с видом на парк Галицкого и стадион. Отличная точка для фото."
    },
    {
      "name": "Музей военной техники под открытым небом",
      "coordinates": [39.0665, 45.0722],
      "info": "Экспозиция танков, самолётов и другой военной техники на открытом воздухе в районе ЗИП. Интересно для всей семьи."
    }
  ]

data2 = [
    {
        "name": "Olympic Park",
        "coordinates": [39.9602, 43.4022],
        "info": "A complex of sports facilities built for the 2014 Winter Olympics. Includes ice arenas, the Fisht Stadium, and the Olympic Square.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Rosa Khutor",
        "coordinates": [40.2556, 43.6756],
        "info": "Popular ski resort in Krasnaya Polyana. Winter sports in cold months, trekking and cable cars in summer.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },
    {
        "name": "Sochi Sea Terminal",
        "coordinates": [39.7204, 43.5855],
        "info": "Architectural symbol of Sochi with a tower and spire. Serves as departure point for sightseeing boats and yachts.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Riviera Park",
        "coordinates": [39.7198, 43.5911],
        "info": "One of the city's oldest parks with alleys, amusement rides, and a dolphinarium. Great for family recreation.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "SkyPark",
        "coordinates": [39.9111, 43.5944],
        "info": "Extreme adventure park featuring Russia's longest suspension bridge and bungee jumping opportunities.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Sochi Autodrom",
        "coordinates": [39.9575, 43.4038],
        "info": "Modern Formula 1 racetrack located in the Olympic Park. Hosted the Russian Grand Prix races.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Dendrarium",
        "coordinates": [39.7342, 43.5709],
        "info": "Botanical garden featuring plants from around the world, palm trees, fountains, and a cable car.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Sochi Park",
        "coordinates": [39.9583, 43.3983],
        "info": "Russia's first theme park inspired by Russian fairy tales and folklore. Attractions for both children and adults.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Krasnaya Polyana",
        "coordinates": [40.2106, 43.6761],
        "info": "Mountain resort village known for active recreation and winter sports. One of the Winter Olympics centers.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },
    {
        "name": "Agurskie Waterfalls",
        "coordinates": [39.8475, 43.5556],
        "info": "Picturesque waterfalls in the Agura Gorge near Mount Akhun. Popular destination for hiking.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Krasnodar Stadium",
        "coordinates": [39.0181, 45.0355],
        "info": "Modern football stadium built on initiative of Sergey Galitsky. Known for unique circular architecture and adjacent park.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Galitsky Park",
        "coordinates": [39.0175, 45.0343],
        "info": "One of Russia's most beautiful urban parks. Features modern landscape design, fountains, amphitheater, and recreation areas.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Krasnodar Philharmonic",
        "coordinates": [38.9794, 45.0301],
        "info": "Historic building and center of musical culture. Hosts classical and contemporary music concerts.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Kuban Cossack Choir",
        "coordinates": [38.9887, 45.0332],
        "info": "One of Russia's oldest and most famous folk ensembles. Located in a building with museum and concert hall.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Gorky Central Park",
        "coordinates": [38.984, 45.0274],
        "info": "Historic downtown park with alleys, attractions, pond and concert stage. Popular walking spot for locals.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Krasnaya Street",
        "coordinates": [38.9765, 45.0284],
        "info": "Krasnodar's main street. Becomes pedestrian on weekends. Hosts parades, festivals and public celebrations.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "St. Catherine's Cathedral",
        "coordinates": [38.9799, 45.0339],
        "info": "City's main Orthodox church in Neo-Byzantine style. Named after Saint Catherine.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Chistyakovskaya Grove",
        "coordinates": [39.0001, 45.05],
        "info": "Green zone in city center with century-old trees, playgrounds, mini-zoo and walking paths.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Observation Tower on Zakharova Street",
        "coordinates": [39.0148, 45.0351],
        "info": "Unique viewpoint overlooking Galitsky Park and the stadium. Great spot for photography.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Open-Air Military Equipment Museum",
        "coordinates": [39.0665, 45.0722],
        "info": "Exhibition of tanks, aircraft and other military hardware in ZIP district. Interesting for all ages.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },
    {
        "name": "National Museum of the Republic of Adygea",
        "coordinates": [40.1053, 44.6088],
        "info": "Main museum of Adygea showcasing regional history, culture and nature. Notable for archaeological finds and ethnographic collections.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Gorky Culture and Recreation Park",
        "coordinates": [40.1017, 44.6075],
        "info": "Central city park with green alleys, fountains, amusement rides and summer cafes. Popular for walks and family recreation.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Maykop Cathedral Mosque",
        "coordinates": [40.1036, 44.6102],
        "info": "Beautiful mosque with tall minarets built in traditional Islamic style. One of the city's symbols.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Monument 'Friendship'",
        "coordinates": [40.1089, 44.6115],
        "info": "Memorial symbolizing centuries-old friendship between Adyghe and Russian peoples. Located on scenic square.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Belaya River (Shkhaguashe)",
        "coordinates": [40.095, 44.605],
        "info": "Picturesque river flowing through Maykop. Its banks feature embankments and recreation areas.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Adyghe State University",
        "coordinates": [40.1002, 44.6138],
        "info": "Republic's main university known for its campus with green alleys and modern buildings.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Pushkin City Drama Theater",
        "coordinates": [40.1044, 44.6097],
        "info": "Leading theater in Maykop staging plays based on Russian and world classics, as well as works by Adyghe authors.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_bower_light-0cd5ac1b3f65f79e972f0b4c4d612f75d1827c6160d7e73aeb3d4d7d15100be1.svg?r=0.37890644441789034"
    },
    {
        "name": "Lenin Square",
        "coordinates": [40.1065, 44.6083],
        "info": "Central city square surrounded by administrative buildings. Hosts major municipal events.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_atractions_light-eaa362f1a8ce8828f344fe7345dfbbee5c1c2ab99a5342abcbc09c7666f93915.svg?r=0.37890644441789034"
    },
    {
        "name": "Fiziabgo Mountain",
        "coordinates": [40.2, 44.65],
        "info": "Scenic mountain near Maykop popular with tourists and hiking enthusiasts. Offers excellent city views from summit.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },
    {
        "name": "Maykop Hydroelectric Station",
        "coordinates": [40.09, 44.62],
        "info": "Historic hydroelectric plant built in early 20th century. Notable for its architecture and engineering solutions.",
        "type": "urban",
        "icon": "https://disk.2gis.com/styles/assets/icons/bx-buildings-22ac0cfa3e265e2d6f40c93f10076c76b13b93fdcd8bf7a14915a2fdb2178662.svg?r=0.5357151146252415"
    },
    {
        "name": "Lago-Naki Plateau",
        "coordinates": [39.9369, 44.0514],
        "info": "Picturesque high-mountain plateau with alpine meadows, hiking trails and viewpoints. Popular for trekking and photography.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },
    {
        "name": "Guam Gorge",
        "coordinates": [39.6533, 44.2886],
        "info": "Unique canyon with narrow-gauge railway along the cliff. Features waterfalls, rock formations and relict plants.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Azish-Tau Ridge",
        "coordinates": [40.0012, 44.0987],
        "info": "Part of Caucasus Mountains with caves (Azishskaya, Bolshaya Azishskaya), waterfalls and hiking routes.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },

    {
        "name": "Bolshaya Azishskaya Cave",
        "coordinates": [40.0025, 44.0993],
        "info": "One of Russia's most beautiful caves with stalactites, stalagmites and underground halls. Equipped with lighting and walkways.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Nezhnaya Cave",
        "coordinates": [39.8419, 43.9758],
        "info": "Small but picturesque cave on Lago-Naki Plateau. Known for white calcite formations.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },

    {
        "name": "Rufabgo Waterfalls",
        "coordinates": [40.1475, 44.0736],
        "info": "Cascade of several waterfalls in Belaya River gorge. Most famous is 'Rufabgo's Heart' with stone arch.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Psadskie Waterfalls",
        "coordinates": [38.3594, 44.5412],
        "info": "Group of over 100 waterfalls near Gelendzhik. Many accessible only with guides or off-road vehicles.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },
    {
        "name": "Agurskie Waterfalls",
        "coordinates": [39.6936, 43.5572],
        "info": "Legendary waterfalls near Sochi. Hiking route passes Eagle Rocks with views of Mount Akhun.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },

    {
        "name": "Kardyvach Lake",
        "coordinates": [40.6333, 43.5667],
        "info": "High-mountain turquoise lake at foot of Main Caucasus Ridge. Accessible only by foot or off-road vehicle.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },
    {
        "name": "Mzymta River",
        "coordinates": [40.2833, 43.5667],
        "info": "Longest river in Krasnodar Krai. Known for rafting, canyoning and views of Akhshtyr Gorge.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Abrau Lake",
        "coordinates": [37.5919, 44.6994],
        "info": "Krai's largest freshwater lake near Abrau-Durso winery. Features walking trails and boat rentals.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },

    {
        "name": "Dolmens in Zhane River Valley",
        "coordinates": [38.3583, 44.5083],
        "info": "Mysterious megalithic structures 4-5 thousand years old. Several dolmen groups preserved in the valley.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Akhshtyr Cave",
        "coordinates": [39.8378, 43.5167],
        "info": "Cave with ancient human settlement. Contains archaeological finds and stalactites. Nearby - suspension bridge over Mzymta.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },

    {
        "name": "Panagia Cape",
        "coordinates": [36.7667, 45.2],
        "info": "Wild rocky cape near Taman with mud volcanoes and shell beaches. Place for secluded relaxation.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
    {
        "name": "Dzhanhot Pine Forest",
        "coordinates": [38.2833, 44.5833],
        "info": "Pine forest on Black Sea coast between Divnomorsk and Dzhanhot. Clean air and scenic trails.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/leaf-solid-a3db1f9184c18cc6e3f5129712b4f31adcdb24c65e54389334c9340278c35764.svg?r=0.28953634401752304"
    },

    {
        "name": "Château Le Grand Vostok Vineyards",
        "coordinates": [37.6833, 44.8833],
        "info": "French vineyards in Taman with tasting rooms and sea views. Produces wines using European technologies.",
        "type": "outdoor",
        "icon": "https://disk.2gis.com/styles/assets/icons/poi_flower_light-b76a28d053911de6590eb51a2443d51003dc5f519aca07bf3516f61df05e5db7.svg?r=0.37890644441789034"
    },
]

with open("test.json", "r", encoding="utf-8") as file:
    dataN = json.load(file)



def connect():
    conn = sqlite3.connect("orgs.db")

    return conn

def close(conn):
    conn.close()

def getOrgs():
    conn = connect()
    cursor = conn.cursor()

    text = '''
SELECT * FROM организации
'''
    cursor.execute(text)
    data = []

    for i in cursor.fetchall():
        smallData = {
            "name": i[1],
            "coordinates": [i[2],i[3]],
            "info": i[4],
            "img": i[5]
            }
        data.append(smallData)
    close(conn)
    # with open("test.json", "w", encoding="utf-8") as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)
    return data

def addOrg(data):
    conn = connect()
    cursor = conn.cursor()

    text = '''
INSERT INTO организации (название, широта, долгота, описание, img) VALUES (?,?,?,?,?)
'''
    if ("img" not in data.keys()): cursor.execute(text, (data["name"], data["coordinates"][0], data["coordinates"][1], data["info"], None ))
    else: cursor.execute(text, (data["name"], data["coordinates"][0], data["coordinates"][1], data["info"], data["img"] ))
    conn.commit()
    close(conn)

def insert_audio():
    conn = connect()
    cursor = conn.cursor()

    with open(path + "audio/gorodskoy-port-zvuk-zvuk-41748 (mp3cut.net).mp3", "rb") as file:
        first = file.read()
    with open(path + "audio/nedovolnyie-vozglasyi-na-futbole-34812.mp3", "rb") as file:
        second = file.read()

    for i in range(1,11):
        text = '''
UPDATE организации
SET audio = ?
WHERE ID = ?
'''
        cursor.execute(text, (sqlite3.Binary(first), i ))
    
    for i in range(11,21):
        text = '''
UPDATE организации
SET audio = ?
WHERE ID = ?
'''
        cursor.execute(text, (sqlite3.Binary(second), i))
    conn.commit()
    close(conn)


# insert_audio()

# for i in data2:
#     flag = False
#     for j in dataN:
#         if i["name"] == j["name"]: flag = True
#     if flag == False:
#         dataN.append(i)

# print(dataN)

# for i in dataN:
#     addOrg(i)
# print(f"len = {len(dataN)}")    
# print(f"len2 = {len(data2)}")    

# print(getOrgs())

# with open("test.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     # newdata = []
#     print(data)
#     for i in data:
#       tempo = i
#       tempo["img"] = 
#       if i["img"] == None and :
#           data.remove(i)
#           print(i)
# with open("test.json", "w", encoding="utf-8") as file:
#   json.dump(data, file, indent=4, ensure_ascii=False)        


'''CREATE TABLE "организации" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"название"	TEXT,
	"широта"	REAL,
	"долгота"	REAL,
	"описание"	TEXT,
  "img" TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);'''