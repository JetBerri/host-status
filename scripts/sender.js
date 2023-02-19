const nodemailer = require('nodemailer');
const mjml2html = require('mjml');
const fs = require('fs');

const config = require('./config/credentials.json');

// Leer el archivo MJML
const mjml = fs.readFileSync(config.mjml_path, 'utf-8');

// Convertir el MJML a HTML
const html = mjml2html(mjml).html;

// Configurar el transportador de correo electrónico
const transporter = nodemailer.createTransport({
  service: 'yahoo',
  auth: {
    user: config.sender_email,
    pass: config.sender_password,
  },
});

// Configurar el correo electrónico
const mailOptions = {
  from: config.sender_email,
  to: config.recipient_email,
  subject: config.subject,
  html: html,
};

// Enviar el correo electrónico
transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    console.error(error);
  } else {
    console.log('El correo electrónico ha sido enviado:', info.response);
  }
});