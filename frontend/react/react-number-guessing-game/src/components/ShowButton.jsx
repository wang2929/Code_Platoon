import React from 'react'

export default function ShowButton({reset}) {
    if (reset) {
        return <button className="game" type="reset">Reset</button>
    }
    return (
        <button className="game" type="submit">Submit</button>
    )
}
