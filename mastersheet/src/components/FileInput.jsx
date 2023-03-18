import React from 'react';
import './FileInput.css';

export default function FileInput(props) {
	return (
		<div className="file-input">
			<input type="file" {...props} />
			<label>Select File</label>
		</div>
	);
}