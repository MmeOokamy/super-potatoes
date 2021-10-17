import React, { useState, useEffect} from "react";
import "./App.css";


function App() {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/members").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

    return (
        <div>
            {(typeof data === 'undefined') ? (
                <p>Loading...</p>
            ): (
                data.map((i) => (
                    <p key={i.id}>{i.user_name} - {i.user_power} </p>
                ))
            )}
        </div>
    )
}

export default App