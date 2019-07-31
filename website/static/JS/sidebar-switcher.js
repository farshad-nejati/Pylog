document.addEventListener('DOMContentLoaded', () => {
    let sidebar_switcher = document.getElementById('sidebar');
    document.getElementById('sidebar-switcher').addEventListener('click', () => {
        if(!sidebar_switcher.classList.contains("hide")) {
            sidebar_switcher.classList.add("hide");
            console.log("sidebar-switcher classes:"+ sidebar_switcher.classList + " \n");
        } else {
            sidebar_switcher.classList.remove("hide");
            console.log("sidebar-switcher classes:"+ sidebar_switcher.classList + " \n");
        }
    });
});