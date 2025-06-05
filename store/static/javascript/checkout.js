document.querySelector('.purchase-btn').addEventListener('click', (e) => {
  
  alert('Purchased!')
  setTimeout(() => {
    window.location.reload()
  }, 300)

  submitFormData()
})


const submitFormData = async () => {
  const response = await axios.post('/process_order/', {
  }, {
    headers: {
      'X-CSRFToken': csrftoken
    },
  })

  return response.data
}