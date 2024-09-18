const axios = require('axios');
const express = require('express');
const cheerio = require('cheerio');

async function requisicao(){
    try{
        // Faz a requisição para o site e obtém o HTML
        const response = await axios.get('https://www.pcgamer.com/epic-games-store-free-games-list/');
        const html = response.data;
        
        // Carrega o HTML com o Cheerio
        const $ = cheerio.load(html);
        
        // Seleciona todos os elementos <ul> na página
        const ulElements = $('ul');
        
        
    } catch (error){

    }
}

requisicao();