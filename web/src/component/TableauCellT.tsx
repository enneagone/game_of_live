import {Cell} from "./Cell";
import React from "react";



export const TableauCellT =   (props :{
    graph: {
        alive_cell_points: number[][];
        length: number;
        nb_alive_cell: number;
        width: number;
    }
}) => {
    const graph = props.graph;


    let tab = [];
    let alive_cell_points_str: string[] = [];
    if (graph.alive_cell_points) {
        graph.alive_cell_points.map(
            (va) => alive_cell_points_str.push(va.join('_'))
        )
    }

    for (let y = 0; y < graph.length; y++) {
        let tab_x = []
        for (let x = 0; x < graph.width; x++) {
            if (alive_cell_points_str.includes([y, x].join('_'))) {
                tab_x.push(true)
            } else {
                tab_x.push(false)
            }
        }
        tab.push(tab_x)
    }

    return <>
            <h3>Cellule en vie : {graph.nb_alive_cell}</h3>
            <table  className="table">
                <tbody>
                {tab.map(
                    (value) => <tr> {value.map(
                        (value) => <td className={ value ? "bg-warning" : ""}><Cell alive={value}/></td>
                    )} </tr>
                )}
                </tbody>
            </table>

            </>
}