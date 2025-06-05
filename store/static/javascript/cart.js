const updateBtns = document.querySelectorAll('.update-cart')

updateBtns.forEach(btn => {
  btn.addEventListener('click', (e) => {
    const productId = btn.dataset.product
    const action = btn.dataset.action

    if (user === 'AnonymousUser') {
      console.log('not logged in')
      window.location.href = '/login/';
    }

    if (action === 'remove') {
      alert('Removed from Cart!')
      setTimeout(() => {
        window.location.reload()
      }, 300)
    } else {
      alert('Added to Cart!')
    }

    updateUserOrder(productId, action)
  })
})

const updateUserOrder = async (id, action) => {
  const response = await axios.post('/update_item/', {
    'productId': id,
    'action': action
  }, {
    headers: {
      'X-CSRFToken': csrftoken
    }
  })

  return response.data
}
