import { useEffect, useState } from "react"
import getMyInfos from "../api/infoApi";

const useMyInfos = () => {
    const [myInfo, setMyInfo] = useState([]);

    useEffect(() => {
        const loadMyInfos = async () => {
            const myInfos = await getMyInfos();
            setMyInfo(myInfos);
        };

        loadMyInfos();
    }, []);

    return myInfo;
};

export default useMyInfos;