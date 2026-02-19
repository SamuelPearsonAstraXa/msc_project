const close_search_box = document.querySelector('.close-search');
const open_search_box = document.querySelector('.search-toggle');
const search_box = document.querySelector('.search-box');

$(document).ready(e=>{
    $('.nav-toggle').click(e=>{
        $('.popup-nav').slideToggle(1000)
    })

    $('.close-search').click(e=>{
        $('.search-box').fadeOut(500)
    })

    $('.search-toggle').click(e=>{
        $('.search-box').fadeIn(500)
    })
})