const map = new mapgl.Map("container", {
    key: "326d4810-3f02-457d-928f-d6bd76483dfa",
    center: [38.9759316378123, 45.0402278340586],
    zoom: 7.5,
    styleState: {
        terrainEnabled: true,
    },
});


const sochiLandmarks = [
    {
        name: "Олимпийский парк",
        coordinates: [39.9602, 43.4022],
        info: "Комплекс спортивных сооружений, построенный для зимней Олимпиады 2014 года. Включает ледовые арены, стадион 'Фишт' и олимпийскую площадь.",
    },
    {
        name: "Роза Хутор",
        coordinates: [40.2556, 43.6756],
        info: "Популярный горнолыжный курорт в Красной Поляне. Зимой — катание, летом — треккинг и канатные дороги.",
    },
    {
        name: "Морской вокзал",
        coordinates: [39.7204, 43.5855],
        info: "Архитектурный символ Сочи с башней и шпилем. Отсюда отправляются прогулочные катера и яхты.",
    },
    {
        name: "Парк Ривьера",
        coordinates: [39.7198, 43.5911],
        info: "Один из старейших парков города с аллеями, аттракционами и дельфинарием. Отличное место для семейного отдыха.",
    },
    {
        name: "Скайпарк",
        coordinates: [39.9111, 43.5944],
        info: "Экстремальный парк развлечений с самым длинным подвесным мостом в России и возможностью прыжков с высоты.",
    },
    {
        name: "Сочи Автодром",
        coordinates: [39.9575, 43.4038],
        info: "Современная трасса для Формулы-1, расположенная в Олимпийском парке. Проводились Гран-при России.",
    },
    {
        name: "Дендрарий",
        coordinates: [39.7342, 43.5709],
        info: "Ботанический сад с коллекцией растений со всего мира, пальмами, фонтанами и канатной дорогой.",
    },
    {
        name: "Сочи Парк",
        coordinates: [39.9583, 43.3983],
        info: "Первый тематический парк в России, вдохновлённый русскими сказками и героями. Развлечения для детей и взрослых.",
    },
    {
        name: "Красная Поляна",
        coordinates: [40.2106, 43.6761],
        info: "Курортный посёлок в горах, место активного отдыха и лыжного спорта. Один из центров зимней Олимпиады.",
    },
    {
        name: "Агурские водопады",
        coordinates: [39.8475, 43.5556],
        info: "Живописные водопады в Агурском ущелье недалеко от горы Ахун. Популярное место для пеших прогулок.",
    },
];

const krasnodarLandmarks = [
    {
        name: "Краснодарский стадион",
        coordinates: [39.0181, 45.0355],
        info: "Современный футбольный стадион, построенный по инициативе Сергея Галицкого. Известен уникальной круглой архитектурой и парком рядом.",
    },
    {
        name: "Парк Галицкого",
        coordinates: [39.0175, 45.0343],
        info: "Один из самых красивых городских парков России. Современный ландшафтный дизайн, фонтаны, амфитеатр, зоны отдыха и искусственные холмы.",
    },
    {
        name: "Краснодарская филармония",
        coordinates: [38.9794, 45.0301],
        info: "Историческое здание и центр музыкальной культуры. Здесь проходят концерты классической и современной музыки.",
    },
    {
        name: "Кубанский казачий хор",
        coordinates: [38.9887, 45.0332],
        info: "Один из старейших и известнейших народных коллективов России. Располагается в здании с музеем и концертным залом.",
    },
    {
        name: "Центральный парк имени Горького",
        coordinates: [38.984, 45.0274],
        info: "Исторический парк в центре города с аллеями, аттракционами, прудом и сценой для концертов. Любимое место прогулок горожан.",
    },
    {
        name: "Улица Красная",
        coordinates: [38.9765, 45.0284],
        info: "Главная улица Краснодара. По выходным становится пешеходной. Здесь проходят парады, фестивали и гуляния.",
    },
    {
        name: "Свято-Екатерининский кафедральный собор",
        coordinates: [38.9799, 45.0339],
        info: "Главный православный храм города, построенный в неовизантийском стиле. Назван в честь святой Екатерины.",
    },
    {
        name: "Чистяковская роща",
        coordinates: [39.0001, 45.05],
        info: "Зелёная зона в центре города с вековыми деревьями, детскими площадками, мини-зоопарком и прогулочными дорожками.",
    },
    {
        name: "Смотровая башня на улице Захарова",
        coordinates: [39.0148, 45.0351],
        info: "Необычное место с видом на парк Галицкого и стадион. Отличная точка для фото.",
    },
    {
        name: "Музей военной техники под открытым небом",
        coordinates: [39.0665, 45.0722],
        info: "Экспозиция танков, самолётов и другой военной техники на открытом воздухе в районе ЗИП. Интересно для всей семьи.",
    },
];

const maykopLandmarks = [
    {
        name: "Национальный музей Республики Адыгея",
        coordinates: [40.1053, 44.6088],
        info: "Главный музей Адыгеи, где представлены экспозиции по истории, культуре и природе региона. Особенно интересны археологические находки и этнографические коллекции.",
    },
    {
        name: "Парк культуры и отдыха имени Горького",
        coordinates: [40.1017, 44.6075],
        info: "Центральный парк города с зелёными аллеями, фонтанами, аттракционами и летними кафе. Популярное место для прогулок и семейного отдыха.",
    },
    {
        name: "Соборная мечеть Майкопа",
        coordinates: [40.1036, 44.6102],
        info: "Красивая мечеть с высокими минаретами, построенная в традиционном исламском стиле. Один из символов города.",
    },
    {
        name: "Монумент «Дружба»",
        coordinates: [40.1089, 44.6115],
        info: "Памятник, символизирующий многовековую дружбу адыгского и русского народов. Расположен на живописной площади.",
    },
    {
        name: "Река Белая (Шхагуаше)",
        coordinates: [40.095, 44.605],
        info: "Живописная река, протекающая через Майкоп. На её берегах оборудованы набережные и места для отдыха.",
    },
    {
        name: "Адыгейский государственный университет",
        coordinates: [40.1002, 44.6138],
        info: "Главный вуз республики, известный своим кампусом с зелёными аллеями и современными корпусами.",
    },
    {
        name: "Городской театр драмы имени А.С. Пушкина",
        coordinates: [40.1044, 44.6097],
        info: "Ведущий театр Майкопа, где ставят спектакли по произведениям русской и мировой классики, а также пьесы адыгских авторов.",
    },
    {
        name: "Площадь Ленина",
        coordinates: [40.1065, 44.6083],
        info: "Центральная площадь города, окружённая административными зданиями. Здесь проходят главные городские мероприятия.",
    },
    {
        name: "Гора Физиабго",
        coordinates: [40.2, 44.65],
        info: "Живописная гора недалеко от Майкопа, популярная среди туристов и любителей пеших походов. С вершины открывается прекрасный вид на город.",
    },
    {
        name: "Майкопская ГЭС",
        coordinates: [40.09, 44.62],
        info: "Историческая гидроэлектростанция, построенная в начале XX века. Интересна своей архитектурой и инженерными решениями.",
    },
];

const krasnodarKraiNatureLandmarks = [
    // Горы и ущелья
    {
        name: "Плато Лаго-Наки",
        coordinates: [39.9369, 44.0514],
        info: "Живописное высокогорное плато с альпийскими лугами, пешеходными тропами и смотровыми площадками. Популярное место для трекинга и фотосессий.",
    },
    {
        name: "Гуамское ущелье",
        coordinates: [39.6533, 44.2886],
        info: "Уникальный каньон с узкоколейной железной дорогой вдоль обрыва. Место с водопадами, скалами и реликтовыми растениями.",
    },
    {
        name: "Хребет Азиш-Тау",
        coordinates: [40.0012, 44.0987],
        info: "Часть Кавказских гор с пещерами (Азишская, Большая Азишская), водопадами и маршрутами для походов.",
    },

    // Пещеры
    {
        name: "Большая Азишская пещера",
        coordinates: [40.0025, 44.0993],
        info: "Одна из самых красивых пещер России с сталактитами, сталагмитами и подземными залами. Оснащена подсветкой и дорожками для туристов.",
    },
    {
        name: "Пещера Нежная",
        coordinates: [39.8419, 43.9758],
        info: "Небольшая, но живописная пещера на плато Лаго-Наки. Известна белоснежными кальцитовыми образованиями.",
    },

    // Водопады
    {
        name: "Водопады Руфабго",
        coordinates: [40.1475, 44.0736],
        info: "Каскад из нескольких водопадов в ущелье реки Белая. Самый известный — «Сердце Руфабго» с каменной аркой.",
    },
    {
        name: "Пшадские водопады",
        coordinates: [38.3594, 44.5412],
        info: "Группа из более 100 водопадов недалеко от Геленджика. Многие доступны только с экскурсиями или внедорожниками.",
    },
    {
        name: "Агурские водопады",
        coordinates: [39.6936, 43.5572],
        info: "Легендарные водопады под Сочи. Маршрут проходит через Орлиные скалы с видом на гору Ахун.",
    },

    // Озёра и реки
    {
        name: "Озеро Кардывач",
        coordinates: [40.6333, 43.5667],
        info: "Высокогорное озеро бирюзового цвета у подножия Главного Кавказского хребта. Добраться можно только пешком или на внедорожнике.",
    },
    {
        name: "Река Мзымта",
        coordinates: [40.2833, 43.5667],
        info: "Самая длинная река Краснодарского края. Известна рафтингом, каньонингом и видами на Ахштырское ущелье.",
    },
    {
        name: "Озеро Абрау",
        coordinates: [37.5919, 44.6994],
        info: "Самое большое пресноводное озеро края рядом с винзаводом «Абрау-Дюрсо». Есть тропы для прогулок и прокат лодок.",
    },

    // Дольмены и археология
    {
        name: "Дольмены в долине реки Жане",
        coordinates: [38.3583, 44.5083],
        info: "Загадочные мегалитические сооружения возрастом 4-5 тыс. лет. В долине сохранилось несколько групп дольменов.",
    },
    {
        name: "Ахштырская пещера",
        coordinates: [39.8378, 43.5167],
        info: "Пещера с стоянкой древнего человека. Внутри — археологические находки и сталактиты. Рядом — подвесной мост через Мзымту.",
    },

    // Морские и прибрежные
    {
        name: "Мыс Панагия",
        coordinates: [36.7667, 45.2],
        info: "Дикий скалистый мыс под Таманью с грязевыми вулканами и пляжами из ракушечника. Место для уединённого отдыха.",
    },
    {
        name: "Джанхотский бор",
        coordinates: [38.2833, 44.5833],
        info: "Сосновый лес на берегу Чёрного моря между Дивноморском и Джанхотом. Чистый воздух и живописные тропы.",
    },

    // Виноделие
    {
        name: "Виноградники «Шато Ле Гран Восток»",
        coordinates: [37.6833, 44.8833],
        info: "Французские виноградники в Тамани с дегустационными залами и видами на море. Производят вина по европейским технологиям.",
    },
];

const allLandmarks = [
    ...sochiLandmarks,
    ...krasnodarLandmarks,
    ...maykopLandmarks,
    ...krasnodarKraiNatureLandmarks,
];

const tooltipEl = document.createElement("div");
tooltipEl.id = "tooltip";
tooltipEl.style.position = "absolute";
tooltipEl.style.backgroundColor = "rgba(0, 0, 0, 0.7)";
tooltipEl.style.color = "white";
tooltipEl.style.padding = "5px";
tooltipEl.style.borderRadius = "5px";
tooltipEl.style.display = "none";
tooltipEl.style.pointerEvents = ""; // Это предотвращает блокировку кликов
document.body.appendChild(tooltipEl);

const markers = allLandmarks.map((place) => {
    const marker = new mapgl.Marker(map, {
        coordinates: place.coordinates,
        icon: "https://disk.2gis.com/styles/assets/icons/poi_shootingrange_7_i-857fc4c4a15073fd0bf5ae5c8e88a3393bd6f66916e2687e6eff70a66ab0dfc7.svg?r=0.46028085401990615",
    });

    marker.on("click", () => {
        const titleEl = document.getElementById("info-title");
        const textEl = document.getElementById("info-text");
        const boxEl = document.getElementById("info-box");

        marker.on("click", () => {
            titleEl.textContent = place.name;
            textEl.textContent = place.info;
            boxEl.style.display = "block";
        });
    });

    map.on("click", () => {
        boxEl.style.display = "none";
    });

    marker.on("mouseover", () => {
        tooltipEl.innerHTML = place.name;

        const [x, y] = map.project(place.coordinates);
        const offsetX = 10;
        const offsetY = -20; // учитываем высоту маркера

        tooltipEl.style.left = `${x + offsetX}px`;
        tooltipEl.style.top = `${y - offsetY}px`; // теперь будет точно над маркером
        tooltipEl.style.display = "block";
    });

    marker.on("mouseout", () => {
        tooltipEl.style.display = "none";
    });

    return marker;
});

const clusterer = new mapgl.Clusterer(map, {
    radius: 60,
});

clusterer.load(markers);
