import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [items, setItems] = useState(null);

  const fetchItems = () => {
    axios.get("http://localhost:8000/items").then((r) => {
      setItems(r.data);
    });
  };

  useEffect(() => {
    fetchItems();
    setInterval(() => {
      fetchItems();
    }, 5000);
  }, []);

  return (
    <>
      <div className="m-10">
        <div className="my-10">
          <h1 className="text-3xl font-bold">
            Reverse Proxy, Nginx config, Frontend and Backend app
          </h1>
        </div>

        <div className="flex overflow-auto gap-4">
          {items &&
            items.map((item, index) => {
              return (
                <div
                  key={index}
                  className="w-full max-w-sm min-w-[300px] bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
                >
                  <div>
                    <img
                      className=""
                      src={item.img}
                      alt="logo"
                      style={{ padding: "0px 5px" }}
                    />
                  </div>

                  <div className="p-5">
                    <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                      {item.title}
                    </h5>

                    <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">
                      {item.description}
                    </p>
                  </div>
                </div>
              );
            })}
        </div>
      </div>
    </>
  );
}

export default App;
