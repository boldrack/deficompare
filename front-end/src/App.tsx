import React from 'react';
import './App.scss';
import Navbar from './components/Navbar/Navbar';
// 1. import `ChakraProvider` component
import {Box, Button, ChakraProvider, useColorMode} from "@chakra-ui/react"
import TimeScaleGraph from './components/TimeScaleGraph/TimeScaleGraph';
import ComparisonTable from './components/ComparisonTable/ComparisonTable';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Overview from './pages/Overview/Overview';

function App() {
    return (
        <ChakraProvider>
            <Router>


            <Navbar></Navbar>

                        <Switch>
          {/*<Route path="/about">*/}
          {/*  <About />*/}
          {/*</Route>*/}
          {/*<Route path="/users">*/}
          {/*  <Users />*/}
          {/*</Route>*/}
          <Route path="/">
            <Overview />
          </Route>
        </Switch>
            </Router>
        </ChakraProvider>
    );
}

export default App;
