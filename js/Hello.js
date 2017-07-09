import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'
class Hello extends Component{
  render() {
    const Home = () => (
      <div>
        <h2>Home</h2>
      </div>
    )
    const About = () => (
      <div>
        <h2>About</h2>
      </div>
    )
    const Topics = () => (
      <div>
        <h1>Topics</h1>
      </div>
    )
    return (
      <Router>
        <div>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/topics">Topics</Link></li>
          </ul>
          <Route exact path="/" component={Home}></Route>
          <Route path="/about" component={About}></Route>
          <Route path="/topics" component={Topics}></Route>
        </div>
      </Router>
    );
  }
}

export default Hello;

