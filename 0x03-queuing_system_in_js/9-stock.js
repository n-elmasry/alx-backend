import express from 'express'
import { createClient } from 'redis'
import { kue } from 'kue'
import { promisify } from 'util';

const listProducts = [
    {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]

const client = createClient()
client.on('error', (err) => {
    console.error('Redis Client Error', err);
});

function getItemById(id) {
    return listProducts.find(product => product.Id === id)
}


function reserveStockById(itemId, stock) {
    client.set(`item.${itemId}`, stock)

}

const getCurrentReservedStockById = async (itemId) => {
    return promisify(client.GET).bind(client)(`item.${itemId}`);
  };




const app = express()
const port = 1245

app.get('/list_products', (request, response) => {
    const formatedProducts = listProducts.map(product => ({
        itemId: product.Id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    }));
    response.json(formatedProducts)
})

app.get('/list_products/:itemId(\\d+)', async (req, res) =>  {
    const itemId = Number.parseInt(req.params.itemId);
    const productItem = getItemById(Number.parseInt(itemId));

    if (!productItem) {
        res.status(404).json({ status: 'Product not found' });
        return;
    }
    const reservedStock = await getCurrentReservedStockById(itemId);
    productItem.currentQuantity = productItem.stock - (Number.parseInt(reservedStock || 0));
    res.json(productItem);
});


app.get('/reserve_product/:itemId(\\d+)',  async (req, response) => {
    const itemId = Number.parseInt(req.params.itemId);
    const productItem = getItemById(itemId);

    if (!productItem) {
        response.status(404).json({ status: 'Product not found' });
        return;
    }

    if(productItem.stock < 1) {
        return response.json({ "status": "Not enough stock available", "itemId": itemId})
    }

        productItem.stock -= 1
        reserveStockById(itemId, 1)
        return response.json({"status": "Reservation confirmed", "itemId": itemId})
    }


)

app.listen(port, () => {

})
