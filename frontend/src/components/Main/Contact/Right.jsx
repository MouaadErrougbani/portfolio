import { Box, Button, Typography } from "@mui/material";
import { useState } from "react";
import styles from "./Contact.styles";

function Right() {
  const [email, setEmail] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");

  function clickedHandler() {
    const url =
      `mailto:mouaad.errougbani@gmail.com` +
      `?subject=${encodeURIComponent(subject)}` +
      `&body=${encodeURIComponent(
        `From: ${email}\n\n${message}`
      )}`;

    window.location.href = url;

    setEmail("");
    setSubject("");
    setMessage("");
  }

  return (
    <Box sx={styles.right.box}>
      <Typography sx={styles.right.p}>
        Send Email
      </Typography>

      {/* Email de l'expéditeur */}
      <Typography
        component="input"
        type="email"
        placeholder="Your Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        sx={styles.right.input}
      />

      {/* Objet */}
      <Typography
        component="input"
        placeholder="Subject"
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
        sx={styles.right.input}
      />

      {/* Message */}
      <Typography
        component="textarea"
        placeholder="Write your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        sx={styles.right.textarea}
      />

      <Button
        variant="contained"
        sx={styles.right.button}
        onClick={clickedHandler}
      >
        Send
      </Button>
    </Box>
  );
}

export default Right;