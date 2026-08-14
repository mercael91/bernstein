import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import VocabularyReference from './VocabularyReference';

const Dashboard = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/vocabulary">Vocabulary Reference</Link>
            </li>
          </ul>
        </nav>

        <Route path="/vocabulary" component={VocabularyReference} />
      </div>
    </Router>
  );
};

export default Dashboard;