const cheerio = require("cheerio");
// const express = require("express");
// const axios = require("axios");
require("dotenv").config();

// Environment variable error handling
if (!process.env.WEBSITE_URL){
    console.error("Error: The environment variable 'WEBSITE_URL' is not defined. Please set it before running the application.");
    process.exit(1);
}
const URL = process.env.WEBSITE_URL;

function getGames($) {
    const currentGame = $('#article-body>p:nth-child(13)').text();
    console.log(currentGame);

    const nextGame = $('#article-body>p:nth-child(17)').text();
    // console.log(nextGame);

    const games2024 = $('#article-body>ul:nth-child(23)').children('li').text();
    // console.log(games2024);

    const games2023 = $('#article-body>ul:nth-child(25)').children('li').text();
    // console.log(games2023);

    const games2022 = $('#article-body>ul:nth-child(27)').children('li').text();
    // console.log(games2022);

    const games2021 = $('#article-body>ul:nth-child(29)').children('li').text();
    // console.log(games2021);

    const games2020 = $('#article-body>ul:nth-child(31)').children('li').text();
    // console.log(games2020);

    const games2019 = $('#article-body>ul:nth-child(33)').children('li').text();
    // console.log(games2019);
}

async function getResponse(websiteURL) {
    try {
        // Make the request and save the result in 'response'
        const response = await cheerio.fromURL(websiteURL);
        console.log('Response sucess');

        // Load the HTML content of the response into Cheerio
        const loadedData = cheerio.load(response.html())
        console.log('Loading sucess')

        getGames(loadedData);
        return 0;
        
    } catch (error) {
        throw error;
    }
}

function main() {
    try {
        getResponse(URL);
        
    } catch (error) {
        // Errors handling
        if (error.errno === -3008) {
            console.error('Error' , error.errno + ': Unable to locate the target server. Check your internet connection and the URL');
        } else {
            console.error('Unexpected error:', error.message);
        }
    }
}

// Run the main function
main();
