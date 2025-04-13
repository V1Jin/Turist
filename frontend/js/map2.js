// Заменим статический массив sochiLandmarks на fetch запрос
let sochiLandmarks = [];

// Функция для загрузки данных о достопримечательностях Сочи
async function fetchSochiLandmarks() {
    try {
        const response = await fetch("http://10.2.0.254:5000/api/dataOrgs");
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        // Преобразуем данные с сервера в нужный формат
        sochiLandmarks = data.map(item => ({
            name: item.name,
            coordinates: item.coordinates,
            info: item.info,
            img: item.img
        }));
        
        return sochiLandmarks;
    } catch (error) {
        console.error("Ошибка при загрузке данных о достопримечательностях Сочи:", error);
        return []; // Возвращаем пустой массив в случае ошибки
    }
}
console.log(sochiLandmarks)
// Основная функция инициализации карты
async function initializeMap() {
    // Ждем загрузки данных перед инициализацией карты
    await fetchSochiLandmarks();
    
    const map = new mapgl.Map("container", {
        key: "326d4810-3f02-457d-928f-d6bd76483dfa",
        center: [38.9759316378123, 45.0402278340586],
        zoom: 7.5,
        styleState: {
            terrainEnabled: true,
        },
    });

    // Создаем массив всех достопримечательностей
    const allLandmarks = [
        ...sochiLandmarks
    ];

    // Создаем элемент для подсказки
    const tooltipEl = document.createElement("div");
    tooltipEl.id = "tooltip";
    tooltipEl.style.position = "absolute";
    tooltipEl.style.backgroundColor = "rgba(0, 0, 0, 0.7)";
    tooltipEl.style.color = "white";
    tooltipEl.style.padding = "5px";
    tooltipEl.style.borderRadius = "5px";
    tooltipEl.style.display = "none";
    tooltipEl.style.pointerEvents = "";
    document.body.appendChild(tooltipEl);

    // Создаем маркеры для всех достопримечательностей
    const markers = allLandmarks.map((place) => {
        const marker = new mapgl.Marker(map, {
            coordinates: place.coordinates,
            icon: "./img/point.svg",
        });

        marker.on("click", () => {
            const titleEl = document.getElementById("info-title");
            const textEl = document.getElementById("info-text");
            const boxEl = document.getElementById("info-box");
            console.log(place)
            document.querySelector(".info-title").innerHTML = place.name;
            document.querySelector(".info-text").innerHTML = place.info;
            document.querySelector(".info-pic").setAttribute("src", place.img)
        });

        marker.on("mouseover", () => {
            tooltipEl.innerHTML = place.name;
            const [x, y] = map.project(place.coordinates);
            const offsetX = 10;
            const offsetY = -20;
            tooltipEl.style.left = `${x + offsetX}px`;
            tooltipEl.style.top = `${y - offsetY}px`;
            tooltipEl.style.display = "block";
        });

        marker.on("mouseout", () => {
            tooltipEl.style.display = "none";
        });

        return marker;
    });

    // Создаем кластеризатор
    const clusterer = new mapgl.Clusterer(map, {
        radius: 60,
    });

    clusterer.load(markers);
}

// Инициализируем карту после загрузки страницы
window.addEventListener("load", initializeMap);

// Обработчик клика для видео (оставлен без изменений)
window.addEventListener("click", () => {
    document.querySelector(".fullsize_video").play();
});