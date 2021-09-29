import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Prism from "prismjs";
import "prismjs/themes/prism-tomorrow.css";

export const CodePage = () => {
  const { address } = useParams();
  const [code, setCode] = useState(0);

  useEffect(() => {
    Prism.highlightAll();
  }, []);

  useEffect(() => {
    console.log(address);
    fetch(`/api/code?address=${address}`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setCode(data["single_file"]);
      });
  }, [address]);

  return (
    <div className="Code">
      <pre>
        <code className={`language-javascript`}>{code}</code>
      </pre>
    </div>
  );
};
