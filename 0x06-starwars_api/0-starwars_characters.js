#!/usr/bin/node

const req = reqire('request');
const API_URL = "https://swapi-api.hbtn.io/api";

if (process.argv.length > 2) {
	req(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
		if (err) {
			console.log(err);
		}
		const charUrl = JSON.parse(body).characters;
		const charName = charUrl.map(
			url => new Promise((resolve, reject) => {
				req(url, (promiseError, __, charReqBody) => {
					if (promiseError) {
						reject(promiseError);
					}
					resolve(JSON.parse(charReqBody).name);
				});
			}));
		Promise.all(charName)
			.then(names => console.log(names.join('\n')))
			.catch(allError => console.log(allError));
	});
}
