import { reactive } from 'vue';
import { jwtDecode } from 'jwt-decode';
import axios from 'axios';

const baseUrl = 'http://127.0.0.1:5000';

const state = reactive({
  isLoggedIn: !!localStorage.getItem('token'),
  user: null,
});


const token = localStorage.getItem('token') || null ;

const fetchUser = async () => {
    let stockUser = jwtDecode(localStorage.getItem('token'));
    try {
      const response = await axios.get(`${baseUrl}/api/user/get-user/${stockUser.user_id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      state.user = response.data.user;
    } catch (err) {
      console.error('Error fetching user:', err);
      state.user = null;
    } 
  }; 

const login = (token) => {
    state.isLoggedIn = true;
    localStorage.setItem('token', token);
    fetchUser(); // Fetch user on login
  };
  
  const logout = () => {
    state.isLoggedIn = false;
    localStorage.removeItem('token');
    state.user = null; // Clear user on logout
  };
  
  export { state, login, logout, baseUrl, token, fetchUser };