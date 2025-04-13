document.querySelector(".choose__close_btn").onclick = () => {
    document.querySelector(".choose__overlay").classList.remove("opened");
};

document.querySelector(".header__lang_btn .choose__btn").onclick = () => {
    document.querySelector(".choose__overlay").classList.add("opened");
};