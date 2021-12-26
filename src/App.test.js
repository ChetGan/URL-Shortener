import { render, screen } from '@testing-library/react';
import App from './App';

test('renders URL Shortener title', () => {
  render(<App />);
  const linkElement = screen.getByText(/Url Shortener/i);
  expect(linkElement).toBeInTheDocument();
});
