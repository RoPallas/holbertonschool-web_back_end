class Airport {
    constructor(name, code) {
        this._name = name;
        this._code = code;
    }
    get name() {
        return this._name;
    }
    set name(name) {
        if (typeof name !== 'string') {
            throw TypeError('Name must be a string');
        }
        this._name = name;
    }
    get code() {
        return this._code;
    }
    set code(code) {
        if (typeof code !== 'string') {
            throw TypeError('Code must be a string');
        }
        this._code = code;
    }

    toString() {
        return `[object ${this.code}]`;
    }
}

export default Airport;
