#!/usr/bin/node
// Get the names of characters in a film
const request = require('request');
const util = require('util');
const get = util.promisify(request.get);
const id = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;

async function getCharacter (url) {
  try {
    const response = await get(url);
    let character = response.body;
    if (typeof character === 'string') { character = JSON.parse(character); }
    console.log(character.name);
  } catch (error) {
    console.log(error.message);
  }
}

async function getFilm (url) {
  try {
    const response = await get(url);
    let film = response.body;
    if (typeof film === 'string') { film = JSON.parse(film); }
    return film.characters;
  } catch (error) {
    console.log(error.message);
  }
}

async function main () {
  try {
    const characters = await getFilm(filmUrl);
    for (const character of characters) { await getCharacter(character); }
  } catch (error) {
    console.log(error.message);
  }
}

main();
