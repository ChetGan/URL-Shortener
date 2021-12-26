import React, {useState, useEffect} from 'react';
import axios from 'axios';
import '../App.css';

//truncate spaces
//validate url
const UrlShortener = () => {
    const [longUrl, setLongUrl] = useState();
    const [shortUrl, setShortUrl] = useState();

    const handleLongUrlSubmit = (e) => {
        e.preventDefault();
        try {
            const url = new URL(longUrl);
            if (url.protocol === "http:" || url.protocol === "https:") {
                submit();
            }
            else {
                alert('Please Enter A Valid HTTP/HTTPS URL.');
                setShortUrl();
            }
          } catch (_) {
            alert('Please Enter A Valid HTTP/HTTPS URL.');
            return;  
          }
    }

    useEffect(() => {
        resolve();
    }, []);

    const resolve = () => {
        const slug = (window.location.href).replace('http://localhost:8080/', '');
        console.log(slug);
        if (slug) {
            axios.get('/api/resolve/' + slug)
                .then(res => {
                    if (res.data.isError) {
                        alert(res.data.statusCode + " " + res.data.message + ". Incorrect Slug.");
                    } else {
                        window.location.replace(res.data.originalUrl);
                    }
                })
        }
    }

    const submit = () => {
        axios.post('/api/urls', {
            longURL:longUrl})
            .then(res => {
                console.log(res.data);
                setShortUrl(res.data.shortUrl);
                //alert('Short URL is ' + res.data.shortUrl);
            })
        
    }
    

    return (
        <>
            <div className="App">
                <h1>URL Shortener Application</h1>
                <br/>
                <form onSubmit={handleLongUrlSubmit} className="App-header">
                    <label>
                        Enter Long Url:
                    </label>
                    <br/>
                    <textarea name={longUrl} className='text' onChange={e => setLongUrl(e.target.value.trim())} rows="8" cols="80"></textarea>
                    <br/>
                    <label>
                        <button type='submit' className='button1'>Submit</button>
                    </label>
                </form>
                <label className='text'>
                    <h2>Short URL:</h2> 
                    {shortUrl} 
                </label>
                {shortUrl ? <button className='button2' onClick={() => {navigator.clipboard.writeText(shortUrl)}}>Copy</button>: null}
            </div>
            <short className='bottom'>Chetan Ganipineni, Georgia Tech</short>
        </>
    );
}

export default UrlShortener;