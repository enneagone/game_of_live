import React, { useState} from 'react';

import {Services} from "../http-services";
import {TableauCellT} from "./TableauCellT";

export const TableauCell =   () => {

    const [mygraph, setGraph] =  useState({alive_cell_points:[[1,0],[1,1],[2,1],[1,2],[2,2],[2,3]],length:5,nb_alive_cell:6,width:5});
    const [nbTour, setNbTour] = useState(0)


    const init = async () => {
        Services.getInitPartie().then(
            (results) => setGraph(results.data)
        );
        setInit(<TableauCellT graph={mygraph}/>)
        setNbTour(nbTour+1)
    }

    const [isInit, setInit] = useState(<><button onClick={init}> start</button></>)


    const next = () => {
        const info = {
            start_points: mygraph.alive_cell_points,
            length: mygraph.length,
            width: mygraph.width,
        }
        console.log(mygraph)
        Services.getNext(info).then(
            (results) => setGraph(results.data)
        )
        console.log(mygraph)
        setInit(<TableauCellT graph={mygraph}/>)
        setNbTour(nbTour+1)
    }


    return <div>
        <h2>nb tour : {nbTour}</h2>
        {isInit}
        <button onClick={next}>next</button>
    </div>


}
