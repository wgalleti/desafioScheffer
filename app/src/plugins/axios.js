import axios from 'axios'
import constants from '@/constants'

const _axios = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
})

_axios.interceptors.request.use((config) => {
  delete config.headers['Authorization']
  try {
    const { token } = JSON.parse(localStorage.getItem(constants.AUTH_STORE_KEY))
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
  } catch (e) {
    console.error(e)
  }
  return config
})

export default _axios
