import React from 'react';

export const Cell = (props: {
    alive: boolean
}) => {

    const alive = props.alive

    return <>
        {alive ? <td style={{backgroundColor:'black'}}/>:<td/>}
    </>
}