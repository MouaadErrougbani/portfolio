import { useEffect, useState } from "react"
import getContacts from "../api/contactApi";

const useContacts = () => {
    const [contact, setContact] = useState([]);

    useEffect(() => {
        const loadContacts = async () => {
            const contacts = await getContacts();

            setContact(contacts);
        };

        loadContacts();
    }, []);

    return contact;
};

export default useContacts;