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

function organizeGames($){
    const currentGame = $('#article-body>p:nth-child(13)').text();
    console.log(currentGame);

    const nextGame = $('#article-body>p:nth-child(17)').text();
    console.log(nextGame);

    /*
    for (let i = 2019; i < 2025; i++) {
        let year = i;

        switch (year) {
            case 2019:
                gamesRaw = $('#article-body>ul:nth-child(33)').children('li').text();
                break;
            case 2020:
                gamesRaw = $('#article-body>ul:nth-child(31)').children('li').text();
                break;
            case 2021:
                gamesRaw = $('#article-body>ul:nth-child(29)').children('li').text();
                break;
            case 2022:
                gamesRaw = $('#article-body>ul:nth-child(27)').children('li').text();
                break;
            case 2023:
                gamesRaw = $('#article-body>ul:nth-child(25)').children('li').text();
                break;
            case 2024:
                gamesRaw = $('#article-body>ul:nth-child(23)').children('li').text();
                break;
            default:
                console.log("Incorrect year parameter");
                break;
        }
        console.log(gamesRaw);

        let listedGames = gamesRaw.split(`${year}: `);
        console.log(listedGames);

        /*let split = listedGames[0].split(`${year + 1}: `);
        listedGames[0] = split[1];

        split = listedGames.at(-1).split(`${year - 1}: `);
        listedGames[listedGames.length - 2] = split[0];
        listedGames[listedGames.length - 1] = split[1];

        let months = [/Jan /, /Feb /, /Mar /, /Apr /, /May /, /Jun /, /June /, /Jul /, /July /, /Aug /, /Sep /, /Oct /, /Nov /, /Dec /, /December /];

        listedGames = listedGames.map(game => {
            for (let i = 0; i < months.length; i++) {
                if(game.search(months[i]) !== -1){
                    let part = game.split(months[i]);
                    return part[0];
                }
            }
            return game;
        });
        console.log('Free games of', year + ':\n', listedGames);
    }*/
}

async function getResponse(websiteURL) {
    try {
        // Make the request and save the result in 'response'
        const response = await cheerio.fromURL(websiteURL);

        // Load the HTML content of the response into Cheerio
        const loadedData = cheerio.load(response.html())

        organizeGames(loadedData);
        return 0;
        
    } catch (error) {
        throw error;
    }
}

async function main() {
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
