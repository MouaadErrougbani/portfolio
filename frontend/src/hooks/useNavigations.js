import { useEffect, useState } from "react";
import getNavigations from "../api/navigationApi";

const useNavigations = () => {
    const [navigation, setNavigation] = useState([]);

    useEffect(() => {
        const loadNavigations = async () => {
            const navigations = await getNavigations();

            setNavigation(
                [...navigations].sort(
                    (a, b) => a.position - b.position
                )
            );
        };

        loadNavigations();
    }, []);

    return navigation;
};

export default useNavigations;