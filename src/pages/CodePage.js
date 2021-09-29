import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';


export const CodePage = () => {
    const { address } = useParams()
    const [code, setCode] = useState(0);


    useEffect(() => {
        console.log(address)
        fetch('/api/code?address=0x4512347810').then(res => res.json()).then(data => {
            setCode(data.time);
        });
    }, [address]);

    return (
        <div>
            <code>
                {code}
            </code>
        </div>
    );
}