import React from 'react';
import ReactDOM from 'react-dom';
import UrlShortener from '../urlshortener';
import {unmountComponentAtNode} from "react-dom";
import axios from 'axios';

let container = null;
beforeEach(() => {
  // setup a DOM element as a render target
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  // cleanup on exiting
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

jest.mock("axios");

it("renders without crashing", ()=> {
    const div = document.createElement('div');
    ReactDOM.render(<UrlShortener></UrlShortener>, div)
})

describe('submit', () => {
    it('fetches short URL successfully from the Shortening API', () => {
        const data = {
        data: {isError: false, 
               message: "Success", 
               shortUrl: "http://localhost:8080/219369", 
               statusCode: 200},
        };
  
        axios.get.mockImplementation(() => resolve(data));
    });
  
    it('fetches data unsuccessfully from the Shortening API', () => {
        const errorMessage = 'Network Error';

        axios.get.mockImplementation(() => reject(new Error(errorMessage)));
    });
});

describe('resolve', () => {
    it('fetches original URL successfully from the Shortening API', () => {
        const data = {
            data: {isError:false, 
                message:"Success",
                originalUrl:"https://www.example.com/", 
                statusCode:200},
        };
  
        axios.put.mockImplementation(() => resolve(data));
    });
  
    it('fetches original URL unsuccessfully from the Shortening API', () => {
        const errorMessage = {
            data: {"isError":true, 
                   "message":"Not Found",
                   "statusCode":404}
        };

        axios.put.mockImplementation(() => reject(new Error(errorMessage)));
    });

    it('fetches original URL unsuccessfully from the Shortening API', () => {
        const errorMessage = 'Network Error';

        axios.put.mockImplementation(() => reject(new Error(errorMessage)));
    });
});