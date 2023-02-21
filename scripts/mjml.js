const mjml = require('mjml');
const fs = require('fs');

const mjmlContent = fs.readFileSync('/opt/host-status/scripts/index.mjml', 'utf-8');
const { html } = mjml(mjmlContent);

fs.writeFileSync('/opt/host-status/scripts/mail/mail.html', html);