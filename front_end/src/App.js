import plot from './plot.png';
import graph from './graph.png';
import './App.css';
import react, {useState} from 'react';
import axios from 'axios';

function App() {
	
	fetch('http://127.0.0.1:8000/plot/')
	.then(res => res)
	  .then(
		(result) => {
			//console.log('ddeeeeeeeeeee',result);
			//setImages(result);
		} ,
		(error) => {
		  console.log(error); 
		}
	  );
	  
	fetch('http://127.0.0.1:8000/home/')
	.then(res => res)
	  .then(
		(result) => {
			//console.log('dddddddddddd',result);
			//setPlots(result.body);
		} ,
		(error) => {
		  console.log(error); 
		}
	  );
	
	
  return (
    <div className="App">
      <header className="App-header">
	  <div className="row">
	  
        <img src={graph} className="image_graph" alt="tried" /><img src={plot} className="image_plot" alt="tried" />
		
		</div>
      </header>
    </div>
  );
}

export default App;

