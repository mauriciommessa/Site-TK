//PIX
//importando o mercadopago
import { loadMercadoPago } from "@mercadopago/sdk-js";

await loadMercadoPago();
const mp = new window.MercadoPago("APP_USR-4e8db518-5a35-422d-990a-ca9985c36bcb");

//obtendo tipos de documento
(async function getIdentificationTypes() {
  try {
    const identificationTypes = await mp.getIdentificationTypes();
    const identificationTypeElement = document.getElementById('form-checkout__identificationType');

    createSelectOptions(identificationTypeElement, identificationTypes);
  } catch (e) {
    return console.error('Error getting identificationTypes: ', e);
  }
})();

function createSelectOptions(elem, options, labelsAndKeys = { label: "name", value: "id" }) {
  const { label, value } = labelsAndKeys;

  elem.options.length = 0;

  const tempOptions = document.createDocumentFragment();

  options.forEach(option => {
    const optValue = option[value];
    const optLabel = option[label];

    const opt = document.createElement('option');
    opt.value = optValue;
    opt.textContent = optLabel;

    tempOptions.appendChild(opt);
  });

  elem.appendChild(tempOptions);
}
